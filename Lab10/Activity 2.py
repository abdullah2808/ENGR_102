# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB10-Activity 2 Plots
# Date: 1 11 2018

import matplotlib.pyplot as plt
import numpy as np
import random

# bar chart of grades
grades = []
for i in range(25):
    grades += [random.randint(80,100)]
print (grades)
y = [3,5,7,4,2,5,8,9,1,2,5,6,7,8,4,3,1,4,5,6,3,4,7,8,4]
# 1
plt.subplot(221)
plt.bar(grades, y)
plt.title("Distribution of Grades")
plt.xlabel("grades")
plt.ylabel("Number of student")
# 2
plt.subplot(222)
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], [ 55, 60, 65, 70, 75, 80, 85, 90, 95, 100] , 'ro')
plt.axis([0, 10, 50, 100])
plt.xlabel('Amount of time studied (hr) ')
plt.ylabel('Student grades')

# 3
x = [60,62,64,66,68,70,72,74,76]
y = [100,112,104,122,96,135,150,114,119]
plt.subplot(223)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.scatter(x,y, marker = "*")
# 4
plt.subplot(224)
plt.plot([0,2,6,8] , [0,20,40,60,])
plt.xlabel('Amount of snickers(pieces)')
plt.ylabel('Amount of sugar (grams)')
# adjustments
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
# 5

x1 = np.linspace(0.0, 30.0)
x2 = np.linspace(0.0, 10.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
plt.figure(2)
plt.subplot(221)
plt.plot(x2, y2, '.-')
plt.title('A pendulum')
plt.xlabel('time (s)')
# 6
plt.subplot(222)
plt.plot([2000, 2004, 2008, 2016, 2024], [8.2, 7.5, 6.9, 6.2, 5.7])
plt.xlabel("Year")
plt.ylabel("Population in Thousands")
plt.title("Snow Leopard Population")

# 7
plt.subplot(223)
days = [1, 2, 3, 4, 5]

dog = [7, 3, 8, 2, 10]
cat = [3, 5, 11, 6, 1]
fish = [5, 9, 12, 7, 11]
snake = [8, 7, 9, 9, 8]

slices = [4, 6, 2, 7]
pets = ["Dogs", "Cats", "Fish", "Snake"]
colors = ['c', 'm', 'r', 'k']

plt.pie(slices, labels=pets, colors=colors, startangle=90, shadow=True)

plt.title("Household Pets")
plt.legend()
#8
plt.subplot(224)
a , b = 50, 25
c = a + b * np.random.random(500)
d, e, f = plt.hist(c,25,density = 1, facecolor = 'r', alpha = 0.50)
plt.xlabel('number of days')
plt.ylabel('feet of rain')
plt.title('Rainfall')
plt.text(45,.3, r'$\mu=100,\ \sigma=15$')
plt.axis([45,80,0,.1])
plt.grid(True)

# adjustments 2
plt.ylabel('right movements and left movements')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.show()




