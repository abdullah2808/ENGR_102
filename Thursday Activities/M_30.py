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

lst = []
n = int(input("Please an enter an integer for a range: "))
for i in range(1,n):
    if (i % 7 == 0) and (i % 5 == 0):
        lst += [i]
print(lst)
