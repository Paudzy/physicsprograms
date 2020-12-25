import math
import random as rand
import matplotlib.pyplot as plt

bottomSpeed = 2
topSpeed = 5
angleChecks = 160

angles = [0] * angleChecks
ranges = [0] * angleChecks

speed = rand.uniform(bottomSpeed, topSpeed)
for angle in range(0,angleChecks):
    angles[angle] = angle
    ranges[angle] = speed ** 2 * math.sin(2 * angle * math.pi / 180) / 9.81

plt.plot(angles, ranges)

speed = rand.uniform(bottomSpeed, topSpeed)
for angle in range(0,angleChecks):
    angles[angle] = angle
    ranges[angle] = speed ** 2 * math.sin(2 * angle * math.pi / 180) / 9.81

plt.plot(angles, ranges)

speed = rand.uniform(bottomSpeed, topSpeed)
for angle in range(0,angleChecks):
    angles[angle] = angle
    ranges[angle] = speed ** 2 * math.sin(2 * angle * math.pi / 180) / 9.81    

plt.plot(angles, ranges)

plt.plot((45,45,45,45,45,45,45),(-3,-2,-1,0,1,2,3)) # Graph of x = 45
plt.plot((90,90,90,90,90,90,90),(-3,-2,-1,0,1,2,3)) # Graph of x = 90
plt.plot((0, angleChecks + 20),(0, 0)) # Graph of y = 0

plt.grid()
plt.show()

    
