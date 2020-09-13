import math
from math import *

# function 1

print ("This shows the evaluation of a sin(x)/(x) evaluated from 1 to 10^-7")
print ("my guess is around .9 ")
print (math.sin(1)/1)
print (math.sin(.1)/.1)
print (math.sin(.01)/.01)
print (math.sin(.001)/.001)
print (math.sin(.0001)/.0001)
print (math.sin(.00001)/.00001)
print (math.sin(.000001)/.000001)
print (math.sin(.0000001)/.0000001)

# function 2
print ("This shows the evaluation of a 1-cos(x)/(x^2) evaluated from 1 to 10^-7")
print ("my guess is around .4 ")
print ((1-(math.cos(1))/1**2))
print ((1-(math.cos(.1)))/(.1**2))
print ((1-(math.cos(.01)))/(.01**2))
print ((1-(math.cos(.001)))/(.001**2))
print ((1-(math.cos(.0001)))/(.0001**2))
print ((1-(math.cos(.00001)))/(.00001**2))
print ((1-(math.cos(.000001)))/(.000001**2))
print ((1-(math.cos(.0000001)))/(.0000001**2))
# function 3
print ("This shows the evaluation of a (1+1/x)^x evaluated from 1 to 10^-7")
print ("my guess is around 2 ")
print ((1+(1/1))**1)
print ((1+(1/.1))**.1)
print ((1+(1/.01))**.01)
print ((1+(1/.001))**.001)
print ((1+(1/.0001))**.0001)
print ((1+(1/.00001))**.00001)
print ((1+(1/.000001))**.000001)
print ((1+(1/.0000001))**.0000001)
