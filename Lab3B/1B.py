# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3B - 1B
# Date: 13/9/18
from math import *
import math

Stress = int(input("Please enter the stress apllied to the material: "))
Cohesion = int(input("Please enter the cohesion of the material: "))
Angle = int(input("Please enter the angle of friction: "))
Shear_Stress = (Cohesion + (Stress*(tan(math.radians(Angle))))) # Mohr-Coulom Failure Criterion
print ("The shear stress is ", Shear_Stress, "given a stress of", Stress, "a cohesion of", Cohesion, "and an angle of", Angle)