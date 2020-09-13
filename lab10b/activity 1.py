# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB10b-Activity 1
# Date: 3 11 2018

import numpy as np
import matplotlib.pyplot as plt

A = 1.00583
B = -0.087156
C = 0.087156
D = 1.00583
X = 1
Y = 0
M = np.array([A, B, C, D]).reshape(2,2)
Vprime = np.array([X,Y])

for i in range(175):
    Vprime = Vprime @ M
    plt.plot(Vprime[0], Vprime[1], "ro")


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Spiral")
plt.show()