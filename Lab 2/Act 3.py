# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Abdullah Ahmad
# Aaron Ehmry
# Harley Ullrich
# Eric Stevelman
# Section: 518
# Assignment: Lab 2 Activity 3
# Date: 4/9/2018

time1 = 30 #sec
time2 = 45 #sec
dist1 = 50 #meters
dist2 = 615 #meters
slope = (615-50)/(45-30) #rise over run
intercept = dist1 - time1 * slope
time3 = 37 #seconds
new_dist = time3 * slope + intercept
print(new_dist)