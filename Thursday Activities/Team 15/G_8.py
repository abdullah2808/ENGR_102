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

string1 = str(input("Please input a string: "))
string2 = ''
for i in range(len(string1)):
    if i % 2 == 0:
        string2 += string1[i]

print (string2)