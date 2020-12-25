import numpy as np

print("Enter the first 3D vector: ")
txt = input()
v1 = txt.split()

print("Enter the second 3D vector: ")
txt = input()
v2 = txt.split()

print("Would you like to the find dot product (d) or cross product (c) or both (b)?")
product = input()

def cross(v1, v2):
    cp_x = float(v1[1]) * float(v2[2]) - float(v1[2]) * float(v2[1])
    cp_y = -1 * (float(v1[0]) * float(v2[2]) - float(v1[2]) * float(v2[0]))
    cp_z = float(v1[0]) * float(v2[1]) - float(v1[1]) * float(v2[0])

    mag = (cp_x ** 2 + cp_y ** 2 + cp_z ** 2) ** 0.5

    cp = (cp_x, -cp_y, cp_z)

    print("v1 x v2 = ", cp)
    print("mag (v1 x v2) = ", round(mag,4))


def dot(v1, v2):
    dp = float(v1[0])*float(v2[0]) + float(v1[1])*float(v2[1]) + float(v1[2])*float(v2[2])
    
    print ("v1 . v2 = ", dp)

if product == "d":
    dot(v1, v2)

elif product == "c":
    cross(v1, v2)

elif product == "b":
    dot(v1, v2)
    cross(v1, v2)

else:
    print("Incorrect input. Restart the program and try again.")



