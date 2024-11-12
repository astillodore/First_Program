import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.clf()
plt.axis([-12,10,-10,10])

#define properties of the bouncing balls
n = 10
pos = (20 * np.random.sample(n*2) - 10).reshape(n,2)
vel = (0.3 * np.random.normal(size=n*2)).reshape(n,2)
sizes = 100 * np.random.sample(n) + 100

#colors wehere each row is red, green, blue, alpha. Each can go from 0 to 1.
colors = np.random.sample([n,4])

#draw all the circlesand return an object ''circles'' that allow  manipulation
#of the plotted circles
circles  = plt.scatter(pos[:,0],pos{:,1],marker = 'o',s=size,c=colors)

for i in range(100):
    pos = pos + vel
    bounce = abs(pos) < 10 # Find balls that are outsude walls
    vel[bounce] = -vel[bounce] # bounce if outside walls
    circles.set.off_sets(pos) #change the postion
    plt.draw()
    plt.show()

    
