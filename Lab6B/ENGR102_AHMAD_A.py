# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB6B-A
# Date: 4 10 2018

# defining variables
n = int(input("Please enter an positive integer: "))
count = 0
lst = []

while n != 1: # runs until n is not equal to 1
    if n % 2 == 0: # checks if n is even and then divides by 2 if it is
        n = n/2
        count += 1 # adds 1 to count to keep tally of iterations
        lst.append(n) # adds the curent value of n to the list
    else: # runs if n is odd and multiplies n by 3 and adds 1
        n = (3 * n)+ 1
        count += 1 # adds 1 to count to keep tally of iterations
        lst.append(n) # adds the current value of n to the list

print ("The numbers in the sequence are", lst)
print ("It took",count,"iterations to reach 1")



