from random import random
from math import pow, sqrt
import matplotlib.pyplot as plt

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
ax = plt.gca()
ax.set_xlim((0,1))
ax.set_ylim((0,1))

SHOTS = 10000
hits = 0
throws = 0

for i in range(SHOTS):
	throws += 1
	x = random()  
	y = random()
	ax.plot(x,y,'o',color='b')
	dist = sqrt(pow(x, 2) + pow(y, 2))
	if dist <= 1.0:
		hits = hits + 1.0
		ax.plot(x,y,'o',color='y')

# hits / throws = 1/4 Pi
pi = 4 * (hits / throws)

print("pi = %s" % (pi))
plt.show()



