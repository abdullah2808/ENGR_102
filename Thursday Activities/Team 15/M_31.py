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

n = int(input("Please enter an integer to find if it is an armstrong number: "))
n2 = str(n)
count = len(n2)
n4 = 0
for i in (n2):
    i = int(i)
    n4 += i**count
if n4 == n:
    print(n, "is a armstrong number")
else:
    print(n, "is not a armstrong number")

