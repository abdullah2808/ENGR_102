# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act3
# Date: 8 11 2018
import math


def prime_factors(n):
    i = 2
    factors = []
    while i * 1 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

x = int(input("Please enter an integar: "))
print(prime_factors(x))