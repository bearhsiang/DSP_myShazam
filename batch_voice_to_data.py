import subprocess
import sys
src = sys.argv[1]
song_list = sys.argv[2]
des = sys.argv[3]
for i in open(song_list, "r"):
	i = i[:-1]
	print("convert", i, "...")
	subprocess.call(["python3", "voice2data.py", src+'/'+i, des+'/'+i[:-4]+'_data'])