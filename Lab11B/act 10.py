# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act10
# Date: 8 11 2018
import numpy as np
import matplotlib.pyplot as plt
height = open('height.out','r')
height_a = []
height_b = []
for i in height:
    b = height.readline()
    c = b.split()
    height_a.append(c)
for i in height_a:
    height_b.append(i[0])
for i in range(0,len(height_b)):
    height_b[i] = float(height_b[i])
print(height_b)
num_bins = 100
n, bins, patches = plt.hist(height_b, num_bins, facecolor='blue', alpha=0.5)
plt.title('height data')
plt.xlabel('independent')
plt.ylabel('height')
plt.annotate('Most probable data occurs at height:150 and x:100', xy=(50,150))
plt.show()