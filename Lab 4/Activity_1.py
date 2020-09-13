# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name:       Ricky Lee
#             Raymond mee
#             Abdullah Ahmad
#             Eric Stevelman
# Section:    518
# Assignment: Lab 4 Activity 1
# Date:       9/25/18

from math import *
print("--------------------------------------------------------------------------------")

print("\n Part 1")
print("#1")
a = 1 / 56
# print(a)
b = 56 * a
# print(b)
c = 2 * a
d = 54 * a
e = c + d
t = e == b
# print(e)
print("If a = 1/56 is 56 * a the same as 2 * a + 54 * a?", t)

print("---------------------")

print("#2")
x = sqrt(1 / 6)
# print(x)
y = x * x * 6
# print(y)
z = x * 6 * x
# print(z)
t = y == z
print("If x = sqrt(1/6) is x * x * 6 the same as x * 6 * x?", t)

print("---------------------")

print("#3")
c = 1 / 3
# print(c)
z = (2 / 3) - c
# print(z)
j = ((c * c * c) / (pow(c, 3))) * c
# print(j)
t = z == j
print("If c = 1/3 is (2 / 3) - (c) the same as ((c * c * c) / (pow(c,3))) * c ?", t)

print("---------------------")

print("#4")
q = 1 / 6
# print(q)
b = ((q * q * q * q) / (pow(q, 4))) * q
# print(b)
L = (1 / 3) - q
# print(L)
t = b == L
print("If q = 1/6 is ((q * q * q * q) / (pow(q, 4))) * q the same as (1 / 3) - (q)?", t)

print("---------------------")

print("#5")
a = 1 / 9
# print(a)
b = sqrt(81) / (sqrt(a / 9))
# print(b)
v = b - 81 + pow(a, -2)
# print(v)
t = b == v
print("If a = 1 / 9 is sqrt(81) / (sqrt(a / 9)) the same as b - 81 + pow(a, -2)?", t)

print("---------------------")

print("#6")
d = (1 / 12) ** 69
# print(d)
g = d / d
# print(g)
f = (12 ** 69) * d
t = g == f
print("If a = (1 / 12) ** 69 is d / d the same as (12 ** 69) * (d)?", t)

print("---------------------")

print("#7")
r = 963 / 18
k = log(r)/log(r)
# print(k)
i = (1 / r)
y = r * i
# print(y)
t = y == k
print("If r = 963 / 18 is log(r) / log(r) the same as r * (1 / r)?", t)

print("---------------------")

print("#8")
y = 1 / 36
# print(y)
z = 6 * y
# print(z)
h = 1 / sqrt(6) / sqrt(6)
# print(h)
t = z == h
print("If y = 1/36 is 6 * y the same as 1 / sqrt(6) / sqrt(6)?", t)

print("--------------------------------------------------------------------------------")

print("\n\n\nPart 2")

tol = pow(10, -13)

a = 1 / (1 + 9)
# print(a)
b = (1 + 9) * a
# print(b)

print("---------------------")

print("#1")
a = 1 / 56
# print(a)
b = 56 * a
# print(b)
c = 2 * a
d = 54 * a
e = c + d
t = abs(e - b)
# print(e)
print("Tolerance: ", tol)
print("If a = 1/56 is 56 * a within the tolerance of 2 * a + 54 * a?", t <= tol)

print("---------------------")

print("#2")
x = sqrt(1 / 6)
# print(x)
y = x * x * 6
# print(y)
z = x * 6 * x
# print(z)
t = abs(y - z)
print("Tolerance: ", tol)
print("If x = sqrt(1/6) is x * x * 6 within the tolerance of x * 6 * x?", t <= tol)

print("---------------------")

print("#3")
c = 1 / 3
# print(c)
z = (2 / 3) - c
# print(z)
j = ((c * c * c) / (pow(c, 3))) * c
# print(j)
t = abs(z - j)
print("Tolerance: ", tol)
print("If c = 1/3 is (2 / 3) - (c) within the tolerance of ((c * c * c) / (pow(c,3))) * c ?", t <= tol)

print("---------------------")

print("#4")
q = 1 / 6
# print(q)
b = ((q * q * q * q) / (pow(q, 4))) * q
# print(b)
L = (1 / 3) - q
# print(L)
t = abs(L - b)
print("Tolerance: ", tol)
print("If q = 1/6 is ((q * q * q * q) / (pow(q, 4))) * q within the tolerance of (1 / 3) - (q)?", t <= tol)

print("---------------------")

print("#5")
a = 1 / 9
# print(a)
b = sqrt(81) / (sqrt(a / 9))
# print(b)
v = b - 81 + pow(a, -2)
# print(v)
t = abs(b - v)
print("Tolerance: ", tol)
print("If a = 1 / 9 is sqrt(81) / (sqrt(a / 9)) within the tolerance of b - 81 + pow(a, -2)?", t <= tol)

print("---------------------")

print("#6")
d = (1 / 12) ** 69
# print(d)
g = d / d
# print(g)
f = (12 ** 69) * d
t = abs(g - f)
print("Tolerance: ", tol)
print("If a = (1 / 12) ** 69 is d / d within the tolerance of (12 ** 69) * (d)?", t <= tol)

print("---------------------")

print("#7")
r = 963 / 18
k = log(r) / log(r)
# print(k)
i = (1 / r)
y = r * i
# print(y)
t = abs(y - k)
print("Tolerance: ", tol)
print("If r = 963 / 18 is log(r) / log(r) within the tolerance of r * (1 / r)?", t <= tol)

print("---------------------")

print("#8")
y = 1 / 36
# print(y)
z = 6 * y
# print(z)
h = 1 / sqrt(6) / sqrt(6)
# print(h)
t = abs(z - h)
print("Tolerance: ", tol)
print("If y = 1/36 is 6 * y within the tolerance of 1 / sqrt(6) / sqrt(6)?", t <= tol)

print("--------------------------------------------------------------------------------")

print("\n\n\nPart 3")
tol = 1 * pow(10, -15)
q = (1 / 12) ** 69
a = q / q
print("a = ", a)
b = (12 ** 69) * d
print("b = ", b)
print("b should be 1, but is not due to a round-off error.\n")
x = 9999999999999999 / 10000000000000000
print("x = ", x)
y = 1
print("y = ", y)
t_a_b = abs(a - b)
t_x_y = abs(x - y)
print("Is a within tolerance of b? ", t_a_b <= tol)
print("Is x within tolerance of y? ", t_x_y <= tol)
