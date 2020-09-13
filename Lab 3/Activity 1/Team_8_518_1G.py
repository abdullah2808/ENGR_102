# By submitting this assignment, all team members agree to the following:
# # “Aggies do not lie, cheat, or steal, or tolerate those who do”
# # “I have not given or received any unauthorized aid on this assignment”
# #
# # Names: Abdullah Ahmad
# # Raymond Mee
# # Ricky Lee
# # Eric Stevelman
# # Section: 518
# # Assignment: Lab 3 1G
# Date: 16/9/18

import math
Voltage = int(input("Enter voltage as an input "))
PowerGain = 20 * math.log10(Voltage) # Db=20logbase10(V)
PowerGain = int(PowerGain)
print (PowerGain)