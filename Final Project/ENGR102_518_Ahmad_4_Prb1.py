# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: FINAL PROJECT
# Date: 11 30 2018

from ENGR102_518_Ahmad_4_all import *

# opens equations and determines interval
equations = open("equations" , 'r') # opens the equations file
n1 = int(input("Please enter first number of interval: "))
n2 = int(input("Please enter second number of interval: "))

interval = (n1, n2) # creates the interval as a tuple
subinterval = 200000.0 # subinterval hard coded

# this next part finds and computes the area of all the equations and plots all of them each figure most be closed for the next figure to open
for i in range(7):
    y = equations.readline()
    trap_int(y, interval, subinterval)
    print("Please close the figure to continue with the program")
    plotter(y, interval)






