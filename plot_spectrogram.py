import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import sys
if len(sys.argv) != 2:
	print("usage: python3 plot_spectogram.py [input_voice]")
	sys.exit(9)
y, sr = librosa.load(sys.argv[1], sr = 8000)
print(sr)
plt.figure(figsize=(6, 4))
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, y_axis='linear', sr = 8000)
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')
plt.show()
