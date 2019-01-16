SONG_SOURCE = ./song_source
HASH = ./hash
DATA = ./data
CENTER = ./center
SORT = ./sort
TARGET = sample
USR = ./usr
REC = ./rec
SOUR = sample.wav
all:
	gcc data2hash.c -o data2hash
	gcc sort_hash.c -o sort_hash
	mkdir -p $(HASH)
	mkdir -p $(DATA)
	mkdir -p $(CENTER)
	mkdir -p $(SORT)
	mkdir -p $(USR)
	mkdir -p $(REC)

build: all create_data_all create_hash_all sort_all
	@echo Build Data Completed!

create_data_all:
	ls $(SONG_SOURCE) > song_list
	python3 batch_voice_to_data_para.py $(SONG_SOURCE) song_list $(DATA)

create_hash_all:
	ls $(DATA) > data_list
	python3 batch_data_to_hash.py $(DATA) data_list $(CENTER) $(HASH)

sort_all:
	ls $(HASH) > hash_list
	python3 batch_sort_hash.py $(HASH) hash_list $(SORT)

record:
	python3 rec_unlimited.py $(USR)/$(TARGET).wav

test:
	@echo Source: $(SOUR)
	python3 voice2data.py $(SOUR) $(USR)/$(TARGET)_data
	./data2hash $(USR)/$(TARGET)_data $(USR)/$(TARGET).center $(USR)/$(TARGET).hash
	./sort_hash $(USR)/$(TARGET).hash $(USR)/$(TARGET).sort
	python3 score.py $(USR)/$(TARGET).sort > $(REC)/$(TARGET).result

clean:
	rm -f data2hash
	rm -f sort_hash
	rm -rf $(HASH)
	rm -rf $(DATA)
	rm -rf $(CENTER)
	rm -rf $(SORT)
	rm -rf $(USR)
	rm -rf $(REC)