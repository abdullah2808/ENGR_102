# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act4
# Date: 8 11 2018
import numpy as np
A = open("doi.txt", 'r')
B = open("un.txt", 'r')
ListA = (A.read().strip().split(" "))
ListB = (B.read().strip().split(" "))

count = 0
Words = []
for Word in set(ListA):
    for Word2 in set(ListB):
        if Word == Word2:
            Words.append(Word)
            count += 1
print("Amount of common words:",count)
print("Common words:", Words)