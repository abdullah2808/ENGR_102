# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3B - 3A
# Date: 13/9/18
import math

nside = int(input("Please enter the amount of sides: "))
lside = int(input("Please enter the length of a side: "))
perim = nside * lside # calculates perimeter
apothem = lside / (2 * (math.tan(math.radians(180/nside))))  # calculates the apothem
area = (apothem * perim) / 2 # finds the area
print ("The area of a polgyon with", nside, "sides and a side length of", lside, "is", area)

intangle = ((nside-2)*180)/nside
print ("The interior angle of the polygon is ", intangle)

inscircle = 2* ((lside)/(2*(math.tan((3.14/nside)))))
circircle = 2 * ((lside)/(2*(math.sin((3.14/nside)))))

print ("The inscribed circle diameter is ", inscircle)
print ("The circumscribed circle diameter is ", circircle)