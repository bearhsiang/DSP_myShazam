import subprocess
import sys
data_dir = sys.argv[1]
data_list = sys.argv[2]
cent_dir = sys.argv[3]
hash_dir = sys.argv[4]
for i in open(data_list, "r"):
	i = i[:-1]
	print("create hash:", i, "...")
	subprocess.call(["./data2hash", data_dir+'/'+i, cent_dir+'/'+i[:-5]+'.center', hash_dir+'/'+i[:-5]+'.hash'])