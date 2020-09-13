# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3B - 1D
# Date: 13/9/18

arrival = int(input("Please enter the arrival rate: "))
service = int(input("Please enter the service rate: "))
row = (arrival/service) # M/M/1 Q
avglength = (row**2)/(1-row)
print ("The average length of the an M/M/1 queue with a given arrival of", arrival, "and a given service rate of", service, "is", avglength)