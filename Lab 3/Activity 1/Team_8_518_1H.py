# By submitting this assignment, all team members agree to the following:
# # “Aggies do not lie, cheat, or steal, or tolerate those who do”
# # “I have not given or received any unauthorized aid on this assignment”
# #
# # Names: Abdullah Ahmad
# # Raymond Mee
# # Ricky Lee
# # Eric Stevelman
# # Section: 518
# # Assignment: Lab 3 1H
# Date: 16/9/18

E1 = float(input("Please enter the richter value of earthquake 1 "))
E2 = float(input("Please enter the richter value of earthquake 2 "))
Diff = E2 - E1
Diff = abs(Diff)
E = 10 **  Diff
print (E)