import random as rand
import math
import matplotlib.pyplot as plt

trials = 1000
radius = 5
inCircle = 0
i = 1
trial = [0] * trials
approx = [0] * trials
error = [0] * trials


for i in range(trials):
    rand_x = rand.uniform(0, radius)
    rand_y = rand.uniform(0, radius)


    hyp = (rand_x ** 2 + rand_y ** 2) ** 0.5

    if hyp <= radius:
        inCircle += 1

    pi = 4 * inCircle / (i+1)
    print("Trial ", i+1)
    print ("Pi ~ ", pi, "\n")

    trial[i] = i
    approx[i] = pi

    percentError = abs(pi - math.pi) * 100.0 / math.pi 
    error[i] = percentError

#piPlot = plt.figure(1)
plt.plot((0, trials + 15), (math.pi, math.pi)) # y = pi
plt.plot(trial,approx) # pi approximation graph

#errorPlot = plt.figure(2)
plt.plot(trial, error) # percent error graph

plt.grid()
plt.show()

print("Final Pi ~ ", pi)
print ("Final percent error ~ ", round(percentError, 5), "percent.")
    
     
    
