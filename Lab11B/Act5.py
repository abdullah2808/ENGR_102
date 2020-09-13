# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act5
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
print(temp2)
for i in range(len(mon)):
    mon[i] = float(mon[i])
    day[i] = float(day[i])
    temp1[i] = float(temp1[i])
    temp2[i] = float(temp2[i])
print(temp2)
plt.axis([0, 8800, 0, 100])

plt.plot(temp1, 'bs', markersize = 2.25, label = "Boston")
plt.plot(temp2, 'gs', markersize = 2.25, label = "Houston")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Houston and Boston Temperatures")
plt.legend()
plt.show()

