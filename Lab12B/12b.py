# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB12B
# Date: 11 25 2018

import turtle

def userinput():# Uses user input to ask for a number
    number = int(input("Please enter an integar: "))
    return number
num = userinput()

def fifths(x): # Divides into 5th taking into account the remainder
    remainder = x % 5
    groups = x // 5
    return remainder, groups


num5 = fifths(num)

turtle.width(width=3)
turtle.speed(0)
def drawsingles(): # Draw a single tally
    turtle.pendown()
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.left(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(15)
def drawgroups(): # Draw the groups of tallies
    for i in range(4):
        drawsingles()
    turtle.backward(60)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(65)
    turtle.penup()
    turtle.left(45)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(45)
    turtle.right(90)
x = 0
for i in range(num5[1]): # Create a for loop to take in the previous functions and run them corresponding times
    drawgroups()
    x += 1
    if x > 3:
        x = 0
        turtle.right(90)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(285)
        turtle.right(180)

for i in range(num5[0]): # Create a for loop to take in the previous functions and run them corresponding times
    drawsingles()
turtle.done()

