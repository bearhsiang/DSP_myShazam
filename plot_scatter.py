import matplotlib.pyplot as plt
import sys
import numpy as np

if len(sys.argv) != 2:
	print("usage: python3 plot_scatter.py [target.center]")
	sys.exit(0)
x = []
y = []
for i in open(sys.argv[1], 'r'):
	# print(i)
	point = i.split(' ')
	x.append(point[0])
	y.append(point[1])
x = np.array(x, dtype = 'float')
y = np.array(y, dtype = 'float')
plt.figure(figsize=(6, 4))
plt.ylim(0, 4000)
# print(x)
# plt.axis([0, 80, 0, 200])
plt.plot(x, y, 'bo')
plt.show()