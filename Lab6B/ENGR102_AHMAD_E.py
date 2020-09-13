# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB6B-E
# Date: 4 10 2018
import math

#defining variables
pi = 0
k = 0 # summation variable
a = 0
while a == 0:
    pi += (((-1) ** k)/((2 * k) + 1)) # the summation
    k += 1 # increases the iteration by 1
    if (abs(pi - (math.pi/4))) < 1E-6: # checks if the absolute value of pi - math.pi is less than the tolerance value
        a += 1 # stops the loop
    else:
        continue # continues the loop

print ("The estimated value of pi is",pi*4,"which was computed with", k, "terms")
print ("The math module value of pi is:", math.pi)

