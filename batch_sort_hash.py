import subprocess
import sys
hash_dir = sys.argv[1]
hash_list = sys.argv[2]
sort_dir = sys.argv[3]

for i in open(hash_list, "r"):
	i = i[:-1]
	print("sorting", i, "...")
	subprocess.call(["./sort_hash", hash_dir+'/'+i, sort_dir+'/'+i[:-5]+'.sort'])