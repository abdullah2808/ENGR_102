# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Abdullah Ahmad
# Section: 518
# Assignment: LAB 4 Activity 2
# Date: 23 / 9 / 18

a = int(input("Please enter either 1 (for true) or 0 (for false) for A: "))
b = int(input("Please enter either 1 (for true) or 0 (for false) for B: "))
c = int(input("Please enter either 1 (for true) or 0 (for false) for C: "))
a = bool(a)
b = bool(b)
c = bool(c)

print ("#1", a and b and c) # 1
print ("#2", a or b or c) # 2
print("#3", ( not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)) # 3
print ("#4",( not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b)))))   # 4
print ("#5", (a or b) and (not (a and b)))   # 5
print ("#6",( a and not b and not c)or(b and not a and not c)or(c and not a and not b)or(a and b and c)) #6
print ("#7",(not((not a and b and c)or(a and b and not c) or (a and b and c)))) # 7
print ("#8", (not((not a and b and c) or (not a and b and not c)))) # 8






