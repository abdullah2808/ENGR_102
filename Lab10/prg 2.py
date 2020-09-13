import matplotlib.pyplot as plt
import numpy as np
import csv
x = []
y = []
with open('paradata.csv', 'r') as csvfile:
    for i in csvfile:
        a = csvfile.readline
        x.append(a)
print(x)
plt.plot(x,y)
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.title('NASA KC135 Acceleration Data')
plt.legend()
plt.show()