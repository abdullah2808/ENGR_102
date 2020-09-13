# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB9B-Act1Prog1
# Date: 11 10 2018

#writes to a file

FileName = input("Please input a file name: ")
FileName2 = FileName + ".txt"
XVar = input("Please enter the name of your x variable: ")
YVar = input("Please enter the name of your y variable: ")
Vars = int(input("Please enter the amount of your x and y variables: "))
DataFile = open(FileName2, "w") #Creates a file to write to

# inputs the data to a file
for i in range(Vars):
    xinput = str(input("Please enter your x variable: "))
    yinput = str(input("Please enter your y variable: "))
    DataFile.write(XVar + ":" + xinput + "\n")
    DataFile.write(YVar + ":" + yinput + "\n")
DataFile.close()