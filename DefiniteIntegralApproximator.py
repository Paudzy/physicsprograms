import matplotlib.pyplot as plt
import random as rand
import math
import numpy as np

#print("Enter the lower bound of integration: ")
#lowerBound = int(input())
#print("Enter the upper bound of integration: ")
#upperBound = int(input())
#print("How many trials would you like to run? (Recommended: 25,000 - 150,000) ")
#trials = int(input())

lowerBound = -1
upperBound = 1
trials = 150000

# Function to integrate
def func(x):
    dartY = x   # f(x)
    return dartY

# Constant variables
underFunc = 0
#-------------------------------------------------------------------------------------

# Generate the function we're integrating
x = np.arange(lowerBound, upperBound, 0.001)

y = [0] * len(x)
for j in range(len(x)):
    y[j] = func(x[j])


# Find f_max and f_min
if max(y) > 0 and min(y) < 0:
    f_max = max(y) * 1.01
    f_min = min(y) * 1.01

elif max(y) > 0 and min(y) > 0:
    f_max = max(y) * 1.01
    f_min = -0.01

elif max(y) < 0 and min(y) < 0:
    f_max = 0.01
    f_min = min(y) * 1.01
    
elif max(y) > 0 and min(y) == 0:
    f_max = max(y) * 1.01
    f_min = -0.01
    
elif max(y) == 0 and min(y) < 0:
    f_max = 0.01
    f_min = min(y) * 1.01

# Create arrays for the randomly generated points
xArray = [0] * trials
yArray = [0] * trials

for i in range(trials):
    
    # Choose random point
    randX = rand.uniform(lowerBound, upperBound)   
    randY = rand.uniform(f_min, f_max)

    # If function is above x-axis, and the random y-value is bounded
    # by function and x-axis:
    if func(randX) > 0 and randY < func(randX) and randY > 0:
        underFunc += 1

        xArray[i] = randX
        yArray[i] = randY

    # If function is below x-axis, and the random y-value is bounded
    # by function and x-axis
    elif func(randX) < 0 and randY > func(randX) and randY <= 0:
        underFunc -= 1
              
        xArray[i] = randX
        yArray[i] = randY


areaRect = abs(upperBound - lowerBound) * abs(f_max - f_min)
totalArea = areaRect * underFunc / i
print("Total Area ~", totalArea)

plt.plot(xArray, yArray, 'yo', markersize = 1)
plt.plot(x, y, 'r')
plt.plot((lowerBound * 1.15, upperBound * 1.15), (0, 0), 'b')
plt.grid()
plt.show()
    
    

    
