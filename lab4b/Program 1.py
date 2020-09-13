# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4B Program 1
# Date: 20 / 9 / 18

numb1 = float(input("Please enter a number: "))
numb2 = float(input("Please enter a number again: "))
numb3 = float(input("Please enter a number again: "))

if ((numb2 > numb1) and (numb2 > numb3)): # if num 2 is the greatest
    print (numb2, "is the greatest")
elif ((numb1 > numb2) and (numb1 > numb3)): # if num 1 is the greatest
    print(numb1, "is the greatest")
elif ((numb3 > numb2) and (numb3 > numb1)): # if num 3 is the greatest
    print(numb3, "is the greatest")



