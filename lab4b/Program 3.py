# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4B Program 3
# Date: 20 / 9 / 18

#inputs
FVelocity = float(input("Please enter fluid velocity: "))
Visc =  float(input("Please enter kinematic viscosity:" ))
LinearDim = float(input("Please enter a characteristic linear dimension: "))


Reynolds = ((FVelocity*LinearDim)/Visc) #calculates Reynolds

print ("The Reynolds number is", Reynolds) #
if Reynolds < 2300:
    print ("The flow is laminar")
elif 2300 < Reynolds < 4000:
    print ("The flow is transient")
elif Reynolds > 4000:
    print ("The flow is turbulent")

print ("https://www.engineeringtoolbox.com/laminar-transitional-turbulent-flow-d_577.html")