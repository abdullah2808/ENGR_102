# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4B Program 4
# Date: 20 / 9 / 18
import math
import cmath #complex math

# inputs and variables
print ("A quadratic equation is an equation of the form Ax2+Bx+C")
a = float(input("Please enter the A value: "))
b = float(input("Please enter the B value: "))
c = float(input("Please enter the C value: "))

d = b**2-4*a*c # finding discriminant

if d < 0: # if D is less than 0 there are imaginary solutions
    x = (-b+cmath.sqrt(d))/2*a
    x2 = (-b-cmath.sqrt(d))/2*a
    print ("This equation has no real solution, but two imaginary solutions: ", x, "or", x2)
elif (a == 0) and (b == 0) and (c == 0): # all coefficients are 0
    print ("There are infinite solutions because y = 0 is a horizontal line at 0.")

elif (a ==0) and (b == 0): # if C is constant no roots
    print ("There are no solutions because the line never crosses the x axis because C is constant")

elif d == 0: # If D is equal to 0 there is 1 root
    x = (-b+math.sqrt(d))/2*a
    print ("This equation has one solutions: ", x)

elif d > 0: # If D is a positive # there is 2 roots
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    print ("This equation has two solutions: ", x1, " or", x2)

