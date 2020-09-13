# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act11
# Date: 8 11 2018

# part A

from math import *


def box_volume(length, width, height, radhole):
    vol = 0
    box = length * width * height
    hole = pi * radhole * radhole
    volume = box - hole
    return volume


print(box_volume(2, 5, 4, 1))

# part B

names = ['Fac 1', 'Fac 2', 'Fac3']
cost = [100,500,200]
product_value = [150,560,400]

def lprofit():
    profit = []
    min = 100000000000
    index = 0
    for i in range(0,len(cost)):
        profit.append(product_value[i] - cost[i])
    for i in range(0, len(profit)):
        if profit[i] < min:
            min = profit[i]
            index = i

    return names[index], profit[index]

print(lprofit())

# part c

time = [1,2,3,4,5]
dist = [9,18,31,35,44]

def avg_vel(list1, list2):
    avg_velocity = []
    for z in range(0,len(list1) - 1):
        avg_velocity.append((list2[z + 1] - list2[z]) / (list1[z + 1] - list1[z]))
    return avg_velocity

print(avg_vel(time,dist))



