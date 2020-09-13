# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3B - 1C
# Date: 13/9/18

Days = int(input("Please enter the amount of days of production: "))
Initial = int(input("Please enter the initial production of the well: "))
Decline = int(input("Please enter the decline rate of the well: " ))
HyperCons = .8
Arps = (Initial/((1 + (HyperCons  * Decline * Days ))**(1/HyperCons )))
print ("The production of a well after", Days, "days and with a hyperbolic constant of .8 is", Arps) # ARPS EQUATION
