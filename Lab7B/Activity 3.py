# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB7B-Act3
# Date: 11 10 2018

users = int(input("Please enter amount of users: "))
directory = {}
unlock = 0
for i in range(users): # records all usernames and passwords
    username = str(input("Please enter a username: "))
    password = str(input("Please enter a password: "))
    directory[username] = password

#print statements
print("All usernames and passwords have been recorded.")
print("You may know attempt to log in.")

while unlock == 0: #loops until a correct combo has been entered
    username = str(input("Please enter a username: "))
    password = str(input("Please enter password: "))
    if directory.get(username) == password: # checks key value
        print("You have been logged in.")
        unlock += 1
    else: # if the key combo is incorrect
        print("Sorry password/username combo doesn't exist.")
        print("Try again.")
        continue

# Test Case
# 2 users
# username: Abdullah password: Ahmad
# username: Yanessa Password: vea
# test case to login is username: Turkey password: Thanksgiving
# results are that it doesn't let you login until you enter one of the above username and password combos.