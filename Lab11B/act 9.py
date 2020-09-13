# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act9
# Date: 8 11 2018
import numpy as np
import matplotlib.pyplot as plt
import re
time = []
al28 = []
al29 = []
data = []
with open('Al_decay.txt','r',encoding='utf-8-sig') as f:
    for i in f:
        i = i.strip()
        update = re.sub(' +', ' ', i)
        data += update.split("\t")
        time.append(data[0])
        al28.append(data[1])
        al29.append(data[2])
        data = []
print(time)
print(al28)
time.remove(time[0])
al28.remove(al28[0])
al29.remove(al29[0])
for i in range(len(al28)):
    time[i] = float(time[i])
    al28[i] = float(al28[i])
    al29[i] = float(al29[i])
plt.plot(time, al28, label = "Al28")
plt.plot(time, al29, 'g-.', label = "Al29")
plt.axis([0,2400,0,2000])
plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Counts")
plt.title("Irradiation of Isotopes of Al over Time")
plt.show()