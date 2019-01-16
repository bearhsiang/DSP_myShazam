import sys
import numpy as np
import matplotlib.pyplot as plt
import os

def hit(a, b):
	if(abs(a[0] - b[0]) > 5):
		return 0
	if(abs(a[1] - b[1]) > 5):
		return 0
	if(abs(a[2] - b[2]) > 0.1):
		return 0
	return 1

def valuate(delta):
	t = [abs(pow(i-np.mean(delta), 3)) for i in delta ]
	return sum(t)
	# delta = np.sort(delta)
	# return delta[-1]*2-delta[-2]


if len(sys.argv) != 2:
	print("usage:./python3 score.py [target.sort]")
	sys.exit(0)
record_entry = []
record_name = sys.argv[1]
for i in open(record_name, "r"):
	record_entry.append(i.split(' '))
record_entry = np.array(record_entry, dtype = 'float')

# print(record_entry)
scores = []
times = []
hash_dir = "./sort"
hash_list = os.listdir(hash_dir)
for hash_file in hash_list:
	# print(hash_file[-5:], file = sys.stderr)
	if(not hash_file.endswith('.sort')): continue
	# print(hash_file, file = sys.stderr)
	check = 0
	hash_entry = []
	for j in open(hash_dir+'/'+hash_file, "r"):
		hash_entry.append(j.split(' '))
	hash_entry = np.array(hash_entry, dtype = 'float')
	h_pt = 0
	r_pt = 0
	delta = np.zeros(3000)
	time = [[] for i in range(3000)]
	while h_pt < len(hash_entry) and r_pt < len(record_entry):
		if hit(hash_entry[h_pt], record_entry[r_pt]):
			check = 1
			# print(hit)
			dt = int(abs(hash_entry[h_pt][3]-record_entry[r_pt][3])*10)
			delta[dt] += 1
			# print(dt, hash_entry[h_pt][3])
			time[dt].append(hash_entry[h_pt][3])
		# if(4000*hash_entry[h_pt][0]+hash_entry[h_pt][1] > \
		# 		4000*record_entry[r_pt][0]+record_entry[r_pt][1]):
		# 		r_pt += 1
		# else:
		# 	h_pt += 1

		for i in range(3):
			if hash_entry[h_pt][i] > record_entry[r_pt][i]:
				r_pt += 1
				break
			elif hash_entry[h_pt][i] < record_entry[r_pt][i]:
				h_pt += 1
				break
			else:
				if i is 2:
					h_pt += 1
					r_pt += 1
					break
	# fig = plt.figure()
	# plt.title(hash_file)
	# plt.plot(delta)
	if not check:
		scores.append(-1)
		times.append(-1)
	else:
		scores.append(valuate(delta))
		times.append(np.median(time[np.argmax(delta)]))
	print(hash_file[:-5], ":", scores[-1], file = sys.stderr)
	
	# plt.show()
	# plt.close(fig)

scores = np.array(scores)
rank = np.argsort(scores)[::-1]
print(record_name)
print("Result")
print("rank\tscore\tsong\ttime(s)")
for i in range(len(rank)):
	print("%d\t%.2f\t%s\t%.2f" % (i, scores[rank[i]], hash_list[rank[i]][:-5], times[rank[i]]))	