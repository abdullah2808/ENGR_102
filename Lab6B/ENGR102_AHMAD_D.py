# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB6B-D
# Date: 4 10 2018

# The last computation takes a while

import math
pi = 0
for k in range (1): # with 1 term
        pi += (((-1) ** k)/((2 * k) + 1)) # the summation
pi *= 4 # the summation returns a value of pi / 4
print ("With 1 term pi is", abs(pi))

pi = 0

for k in range (10): # with 10 terms
        pi += (((-1) ** k)/((2 * k) + 1))
pi *= 4
print ("With 10 terms pi is",abs(pi))

pi = 0

for k in range (100): # with 100 terms
        pi += (((-1) ** k)/((2 * k) + 1))
pi *= 4
print ("With 100 terms pi is",abs(pi))

pi = 0

for k in range (1000): # with 1000 terms
        pi += (((-1) ** k)/((2 * k) + 1))
pi *= 4
print ("With 1000 terms pi is",abs(pi))

pi = 0

for k in range (1000000): # with 1e6 terms
        pi += (((-1) ** k)/((2 * k) + 1))
pi *= 4
print ("With 1e6 terms pi is",abs(pi))

print ("The last computation takes a while")

pi = 0

for k in range (1000000000): # with 1e9 terms
        pi += (((-1) ** k)/((2 * k) + 1))
pi *= 4
print ("With 1e9 terms pi is", abs(pi))

print("The math module value for pi is ", math.pi)

