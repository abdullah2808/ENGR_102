# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3B - 2A
# Date: 13/9/18
import math

obsx = int(input("Please enter the x position of the observer: "))
obsy = int(input("Please enter the y position of the observer: "))
obsz = int(input("Please enter the z position of the observer: "))

p1x = int(input("Please enter the x position of the first point: "))
p1y = int(input("Please enter the y position of the first point: "))
p1z = int(input("Please enter the z position of the first point: "))

p2x = int(input("Please enter the x position of the second point: "))
p2y = int(input("Please enter the y position of the second point: "))
p2z = int(input("Please enter the z position of the second point: "))

veca = math.sqrt(((p1x - obsx)**2)+((p1y - obsy)**2)+((p1z - obsz)**2)) # calculates the vector from observer to first point
veca = abs(veca)
vecb = math.sqrt(((p2x - obsx)**2)+((p2y - obsy)**2)+((p2z - obsz)**2)) # calculates the vectrom from observer to second point
vecb = abs(vecb)

vecai = p1x - obsx
vecaj = p1y - obsy
vecak = p1z - obsz # caclulates I J and K values for vec a

vecbi = p2x - obsx
vecbj = p2y - obsy
vecbk = p2z - obsz # caclulates I J and K values for vec b

AB = (vecai * vecbi) + (vecaj * vecbj) + (vecak * vecbk)

angle = math.degrees(math.acos(AB/(veca*vecb)))

print ("The angle between the two points from the viewer's perspective is", angle)