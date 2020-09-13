# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: FINAL PROJECT
# Date: 11 30 2018


from ENGR102_518_Ahmad_4_all import *

from scipy.cluster import hierarchy
import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np

files = ['MTHELENA.txt', 'NDFARGO.txt', 'NEOMAHA.txt','NMALBUQU.txt', 'NVLASVEG.txt', 'NYNEWYOR.txt',
         'NYSYRACU.txt', 'OHCLEVEL.txt', 'OREUGENE.txt', 'PRSANJUA.txt', 'TNKNOXVI.txt', 'TXAMARIL.txt',
         'TXHOUSTO.txt', 'WASEATTL.txt', 'WIGREBAY.txt'] #files to open
citynames = []
city = ''
for i in range(len(files)): # loop to remove .txt
    city = files[i][0:8]
    citynames.append(city)
distance = []
for i in range(len(files)): # runs the functions in the other file
    temp = readdata(files[i])
    for i in range(len(temp)):
        temp[i] = float(temp[i])
    distance.append(temp)


X = np.array(eucliddist(distance)).reshape(15,15) # euclidean distance

fig = ff.create_dendrogram(X, orientation='left', labels= citynames) # this part of the code is from plot.ly website modifed a bit to plot my data
fig['layout'].update({'width':1200, 'height':1200})
fig['layout'].update({'title': 'City Temperature Dendrogram'})

py.iplot(fig, filename='Cities')