# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB7B-Act2
# Date: 11 10 2018
import math

# variables
VecA = []
VecB = []
MagA = 0
MagB = 0
AplusB = []
AminB = []
dotprod = 0
dimen = int(input("Please enter the # of dimensions for vectors A and B: "))

#for loops
for i in range(dimen): # collects values for A
    IntA = int(input("Please enter values for Vector A: "))
    VecA += [IntA]
for i in range(dimen): # collects values for B
    IntB = int(input("Please enter values for Vector B: "))
    VecB += [IntB]
for i in VecA: # finds magnitude of Vector A
    MagA += i**2
for i in VecB: # finds magnitude of Vector B
    MagB += i**2
for i in range(dimen): # finds A + B
    AplusB += [VecA[i] + VecB[i]]
for i in range(dimen): # finds A - B
    AminB += [VecA[i] - VecB[i]]
for i in range(dimen): # finds dot product
    dotprod += (VecA[i])*(VecB[i])

# calculations
MagA = math.sqrt(MagA)
MagB = math.sqrt(MagB)

# print statements
print("The magnitude of Vector A is", MagA)
print("The magnitude of Vector B is", MagB)
print("The value of A + B is", AplusB)
print("The value of A - B is", AminB)
print("The dot product of vectors A and B is", dotprod)

#Test case 1
# 2 dimensions
# 4
# 5
# 5
# 6
# magntiude a is 6.4
# magnitude b is 7.8
# value of A + B is [9,11]
# Value of A - B is [-1, -1]
# dot produt is 50

#Test case 2
# 2 dimensions
# 4
# 5
# 6
# 5
# 6
# 7
# magntiude a is 8.7
# magnitude b is 10.4
# value of A + B is [9, 11, 13]
# Value of A - B is [-1, -1, -1]
# dot produt is 92