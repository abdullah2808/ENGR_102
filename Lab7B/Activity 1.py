# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB7B-Act1
# Date: 11 10 2018

initialstr = ''
while initialstr != 'stop': # runs until initial string is equal to stop
    initialstr = str(input("Please enter a string to convert to pig latin or stop to stop: "))
    final = '' # the new string
    first = initialstr[0] # first letter of string
    if initialstr == 'stop':
        continue
    elif first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'y': # vowels
        final = initialstr + 'yay' #string manipulation
        print(final)
    else: # consonants
        final = initialstr[1::] + first +  'ay'
        print(final)

#test cases
#apple = appleyay
#turkey = urkeytay
#stop = ends the program
