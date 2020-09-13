# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB10-Activity 1 Program E
# Date: 1 11 2018


import numpy as np
a = np.array([1,2,3])          #array creation
b = np.array([1.2,2.3,3.4])
print(a)
print(a.dtype)
print(b)
print(b.dtype)

print('------------------')

c = np.array([(1.5,2,3,4),(4,5,6,7)])   #array transformation
print(c)

d = np.zeros((3,4)) #creates an array that has 3 rows of 4 columns of 0's
print(d)

e = np.ones((3,4)) #creates an array that has 3 rows of 4 columns of 1's
print(e)

f = np.empty((3,4)) #creates an array that has 3 rows of 4 columns of random numbers in the computers memory
print(f)

g = np.arange(0,100,10) #same thing as range function, Prints a list from 0 to 100 and counts by 10s
print(g)

h = np.arange(0,10,.5) #same thing as range function, Prints a list from 0 to 10 and counts by .5s
print(h)

i = np.linspace(0,5,10) #creates an array from 0 to 5 and gives 10 numbers in between 0 and 5
print(i)

print('-----------------')

#reshaping arrays
j = np.arange(12)   #creates an array from 0-12
j = j.reshape(3,4)  #reshapes that array into 3 rows with 4 columns each
print(j)

k = np.arange(24)   #creates an array from 0-24
k = k.reshape(2,3,4)  #reshapes that array into 2 sets of 3 rows with 4 columns each
print(k)

print('-------------------')

#basic operations
l = np.array([10,20,30,40,50])
m = np.arange(5)
n = l - m  #subtracts the array "l" and the array "m" with their respective index locations
o = m**2  #it squares each number in the array of "m"
p = l<49  #it checks each number in the array "l" and prints 'true' if the statement is true and 'false' if the statement is false
print(n)
print(o)
print(p)

q = np.array([[1,1],[0,1]])
r = np.array([[2,0], [3,4]])
s = q * r  #miltiplys the arrays together and forms a new array
print(s)

t = np.ones((3,4)) #creates an array of 1's in 3 rows with 4 columns each
t *= 3  #multiplys each of the numbers in the array by 3 resulting in all of the numbers being 3 since the original array printed 1's
u = np.random.random((2,3))

print('-------------------')

#universal operations
v = np.arange(3)
w = np.exp(v)
print(w)
x = np.sqrt(v)
print(x)
y = np.array([2.,-1.,4.])
z = np.add(x,y)
print(z)

print('-------------------')

#linear algebra
aa = np.array([[1.0,2.0],[3.0,4.0]])   #creates two arrays
ab = aa.transpose()  #transposes the two arrays
print(ab)
ac = np.linalg.inv(aa) #
print(ac)

ad = np.eye(2)
ae = np.array([[0.0,-1.0],[1.0,0.0]])
af = ae @ ae   #multiplys the two matrixes together forming one matrix
print(af)
ag = np.trace(ad)
print(ag)

ah = np.array([[5.],[7.]])
ai = np.linalg.solve(aa,ah)
print(ai)

aj = np.linalg.eig(ae)
print(aj)

print('-------------------')
#Activity E
#As a team, we have gone through all required sections of the tutorial, and each team member understands the material

A = np.arange(12).reshape(3,4)
B = np.arange(8).reshape(4,2)
C = np.arange(6).reshape(2,3)
D = np.arange(3).reshape(3,1)
E = A @ B @ C
print(E, "Is E = ABC")
print(np.transpose(E), "Is the transpose of E")
print(np.linalg.solve(E,D), "Is the solved linear system of Ex=D")
