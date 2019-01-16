import librosa
import librosa.display
import numpy as np
import sys

y, sr = librosa.load(sys.argv[1],sr=8000,mono=True)
if len(sys.argv) == 5:
	start = int(sys.argv[3])
	end = int(sys.argv[4])
	# print("convert", start, 'to', end)
	Y = abs(librosa.stft(y[start*sr:end*sr]))
else:
	# print("covert all")
	Y =  abs(librosa.stft(y))
# Y = abs(librosa.stft(y[60*sr:70*sr]))
f = open(sys.argv[2], "w")
n_fft = 2048
# print(Y.shape[1], Y.shape[0])
print(sys.argv[1], file = f)
print(Y.shape[1], Y.shape[0], sr, n_fft, file = f)
for i in range(Y.shape[1]):
	# print(i/sr*(0.25*n_fft), file = f)
	for j in range(Y.shape[0]):
		print(Y[j][i], end = ' ', file = f)
	print("", file = f)
f.close()
