# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB 3 - 3A
# Date: 16/9/18

name = input("Please enter a name: ")
age = int(input("Please enter your age: "))
location = input("Please enter a location: ")
hobby = input("Please enter your preferred hobby: ")
food = input("Please enter your favorite food: ")
age = age / 2
age = int(age)
print (" When you were", age, "you lived really close to", location)
print ("Your best friend told you \n \"Hey get into", hobby, "\b\" and so you started.")
age = int((age / 2) + 1)
print ("After", age, "years you started getting good at", hobby, "\n and became known as", name, "\b.")
print ("You had another friend also named", name, "\b.")
print (" Together with your skills at", hobby, "You guys won a tournament")
print ("After winning the tournament you celebrate together and eat", food, "\b.")