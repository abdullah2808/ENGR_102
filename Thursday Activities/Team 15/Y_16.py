# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: ABDULALH AHMAD
# AARON EHMRY
# ERIC STEVELMAN
# HARLEY ULLRICH
# Section: 518
# Assignment: WEEK 7 THURSDAY ACTIVITIES
# Date: 11 / 10 / 2018
Created_list = []
n = int(input("Enter number of elements:"))
for i in range(1, n + 1):
    b = int(input("Enter element:"))
    Created_list.append(b)
Even_list = []
Odd_list = []
for x in Created_list:
    if (x % 2 == 0):
        Even_list.append(x)
    else:
        Odd_list.append(x)
print("The even list is", Even_list)
print("The odd list is", Odd_list)