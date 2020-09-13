# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4B Program 2
# Date: 20 / 9 / 18

height = float(input("Please enter your height in centimeters: "))
weight = float(input("Please enter your weight in kilograms: "))
BMI = weight / ((height/100) ** 2)
if BMI < 18.5:
    print ("Your BMI is", BMI, "and you are underweight.")
elif 18.5 <= BMI <= 24.9:
    print ("Your BMI is", BMI, "and you are normal or healthy Weight.")
elif 24.9 < BMI <= 29.9:
    print("Your BMI is", BMI, "and you are overweight.")
elif BMI > 29.9:
    print("Your BMI is", BMI, "and you are obese.")