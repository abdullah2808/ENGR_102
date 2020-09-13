# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB6B-B
# Date: 4 10 2018


#defining variables
NumOfMeasures = 0
AvgOfMeasures = 0
NegCheck = 0
Measurement = 0
smallest = None
largest = None

while NegCheck == 0: # runs until a negative number is entered based on the value of neg check which increases when a neg number is entered

    Measurement = float(input("Please enter a measurement: "))

    if Measurement >= 0: # checks if number is larger than 0
        AvgOfMeasures = AvgOfMeasures + Measurement # adds the measurement to the running total of averages
        NumOfMeasures += 1 # counts the numbers for averaging

        if smallest is None or largest is None: # this block of code checks for the largest and smallest values
            smallest = Measurement
            largest = Measurement
        elif Measurement < smallest:
            smallest = Measurement
        elif Measurement > largest:
            largest = Measurement

    else:  # exits the while loop if a negative number is entered
        NegCheck += 1

AvgOfMeasures = AvgOfMeasures / NumOfMeasures # finds the average

#Print statements
print ("The average of the measurements you entered is", AvgOfMeasures)
print ("The highest value is", largest)
print ("The lowest value is", smallest)


