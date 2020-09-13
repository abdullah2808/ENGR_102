# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act6
# Date: 8 11 2018
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
mon = []
day = []
year = []
temp1 = []
data = []
data2 = []
temp2 = []
with open('MABOSTON.txt','r',encoding='utf-8-sig') as f:
    for i in f:
        i = i.strip()
        update = re.sub(' +', ' ', i)
        data += update.split(" ")
        mon.append(data[0])
        day.append(data[1])
        year.append(data[2])
        temp1.append(data[3])
        data = []
with open('TXHOUSTO.txt', 'r', encoding='utf-8-sig') as b:
    for z in b:
        z = z.strip()
        update2 = re.sub(' +', ' ', z)
        data2 += update2.split(" ")
        temp2.append(data2[3])
        data2 = []

writedata = open("cities_temp.txt", 'w')
for i in range(len(mon)):
    writedata.write(mon[i] + " "+ day[i] + ' ' + year[i] + ' ' + temp1[i] +  ' ' + temp2[i] + '\n')