# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: FINAL PROJECT
# Date: 11 30 2018


import numpy as np
import matplotlib.pyplot as plt
import math
import plotly.plotly as py
import plotly.figure_factory as ff
import re
# I used this website for help on trapezodial rule http://www.mathwords.com/t/trapezoid_rule.htm
# I helped a few people such as Isaac, Eric, Mathew, Jtee, and Harley
def  trap_int(equa, limit, width): # finds integral takes in equation, interval, and width
    # Variables needed
    deltax = (limit[-1] - limit[0]) / width # finds the width of each subinterval
    looper = 0
    points = [] # the points that will be plotted will be added to this list
    point = 0 # will be used
    points.append(limit[0])
    area = 0.0
    while looper == 0: # using the interval finds the points to evaluate at and adds them to the point
        if point == 0:
            point = limit[0] + deltax
            points.append(point)
        elif (point + deltax) >= float(limit[-1]):
            looper += 1
            point = point + deltax
            points.append(point)
        else:
            point = point + deltax
            points.append(point)
    x = points[0]
    area += eval(equa)
    x = points[-1]
    area += eval(equa) # finds the inside evaluation before the other points
    for i in range(len(points[0:-1:])): # evaluates inside the bracket
        if i != 0:
            x = points[i]
            area += 2 * eval(equa) # finds the stuff in the []
    area = (deltax / 2) * area # final integration calculation
    print("The area under the curve is: ", abs(area))



def plotter(equa, interval): # I helped Harley with this part of the code
    firstnum = interval[0]
    secondnum = interval[-1]
    yvalues = [] # y values needed for plotting
    xrange = np.arange(firstnum, secondnum, .01) # creates a range of x values for plotting
    for i in range(len(xrange)): # loops through the x values evaulating y at each and adding it into the y list
        x = xrange[i]
        yvalues.append(eval(equa))
    plt.plot(xrange,yvalues) # plots
    plt.ylabel('f(x)')
    plt.xlabel(str(interval))
    plt.title(equa)
    plt.show()


def readdata(filename): # opens files and reads data
    temp  = []
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as b:
        for z in b:
            z = z.strip()
            update2 = re.sub(' +', ' ', z)
            data += update2.split(" ")
            temp.append(data[3])
            data = []
    return temp


def eucliddist(data): # euclidean distance taken by subtracting averages of the cities
    distances = []
    for i in range(len(data)):
        for j in range(len(data)):
            distance = math.sqrt(np.sum(((data[0][i] - data[0][j])**2)/15))
            distances.append(distance)
    return distances
