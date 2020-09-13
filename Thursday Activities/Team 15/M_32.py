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
n = int(input('How many rows of the Pascal Triangle?:'))
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [x + r for x, r in zip(row + y, y + row)]
    return n >= 1
pascal_triangle(n)