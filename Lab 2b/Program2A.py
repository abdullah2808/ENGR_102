# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: Lab2B-prg2A (e.g. Lab 1b-2)
# Date: 6/9/18

# Defining Variables
time1 = 13
X1 = 1
Y1 = 3
Z1 = 7

time2 = 84
X2 = 23
Y2 = -5
Z2 = 10

NewTime = 50
# Finding Slopes
XSlope = (X2-X1)/(time2-time1)
YSlope = (Y2-Y1)/(time2-time1)
ZSlope = (Z2-Z1)/(time2-time1)
# Finding Intercepts
Xintercept =  X1 - (time1 * XSlope)
Yintercept =  Y1 - (time1 * YSlope)
Zintercept =  Z1 - (time1 * ZSlope)
# Finding New Posistions
X3 = NewTime * XSlope + Xintercept
Y3 = NewTime * YSlope + Yintercept
Z3 = NewTime * ZSlope + Zintercept

print ("The X Position is", X3)
print ("The Y Position is", Y3)
print ("The Z Position is", Z3)
