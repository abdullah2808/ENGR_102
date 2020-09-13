# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: Lab2B-1 (e.g. Lab 1b-2)
# Date: 6/9/18



print ("Name: Abdullah Ahmad UIN: 927009064 Section: 518")
print ("I was born in Pakistan")
Resistance = 20
Current = 5
Voltage = Resistance * Current
print (Voltage) # OHMS Law

mass = 100
velocity = 21
Kinetic = (((mass)*(velocity**2))/2)
print (Kinetic) # KINETIC ENERGY

FVelocity = 100
Visc = 1.2
LinearDim = 2.5
Reynolds = ((FVelocity*LinearDim)/Visc)
print (Reynolds) # REYNOLDS NUMBER

Temp = 2000
StefConstant = 5.67E-8
energy = (StefConstant*(Temp**4))
print (energy) # STEFAN-BOLTZMANN LAW

Days = 20
Initial = 100
Decline = 2
HyperCons = .8
Arps = (Initial/((1 + (HyperCons  * Decline * Days ))**(1/HyperCons )))
print (Arps) # ARPS EQUATION



