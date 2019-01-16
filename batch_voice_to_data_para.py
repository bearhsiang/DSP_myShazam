import subprocess
import sys
import threading
src = sys.argv[1]
song_list = sys.argv[2]
des = sys.argv[3]
# for i in open(song_list, "r"):
# 	i = i[:-1]
# 	print("convert", i, "...")
# 	subprocess.call(["python3", "voice2data.py", src+'/'+i, des+'/'+i[:-4]+'_data'])
def v2d(i):
	i = i[:-1]
	print("convert", i, "...")
	subprocess.call(["python3", "voice2data.py", src+'/'+i, des+'/'+i[:-4]+'_data'])

threads = [ 0 for i in range(10)]
l = [i for i in open(song_list, "r")]

for i in range(0, len(l), len(threads)):

	for j in range(len(threads)):
		if( i+j >= len(l) ):
			break

		threads[j] = (threading.Thread(target = v2d, args = (l[i+j], )))
		threads[j].start()

	for j in range(len(threads)):
		if(i+j >= len(l)):
			break
		threads[j].join()
		

print("v2d done")
