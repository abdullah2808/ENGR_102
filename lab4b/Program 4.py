# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4B Program 4
# Date: 20 / 9 / 18

widgets = 0
days = int(input("Please enter the # of days: "))
produced = 0
if 0 < days <= 10: # first 10 days
    widgets = 10
    produced = days * widgets
    print ("Amount of widgets produced:", produced)
elif 11 <= days <= 60: # days 11 to 60

    widgets = 40
    produced = 100 + (widgets * (days - 10)) # after 10 days you already have 100 produced
    print ("Amount of widgets produced:", produced)

elif 61 <= days <= 100: # days 61 to 100
    produced = 2880 - (99 - days) * (100 - days) / 2 # after 100 days you have 2880
    print ("Amount of widgets produced:", produced)
