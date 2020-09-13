# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act2
# Date: 8 11 2018
import numpy as np

C = np.array([10,9,0,13,2,5,3,7,8,1,10,11,12,13,14]).reshape(3,5)
print("Is the array \n", C)
itemindex1 = np.where(C == np.amax(C))
itemindex2 = np.where(C == np.amin(C))
row1 = itemindex1[0] + 1
column1 = itemindex1[1] + 1
row2 = itemindex2[0] + 1
column2 = itemindex2[1] + 1

print("The max value is", np.amax(C), "located at row #", row1, " and column #", column1)
print("The min value is", np.amin(C), "located at row #", row2, " and column #", column2)