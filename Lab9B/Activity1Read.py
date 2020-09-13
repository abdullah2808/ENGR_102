# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB9B-Act1Prog2
# Date: 11 10 2018

# This opens the file in the same way the last program created the file
FileName = input("Please input a file to read from: ")
FileName2 = FileName + ".txt"
DataFile = open(FileName2, "r") #reads from a file
XData = []
YData = []
Data = []

# These for loops seperate the data created from the previous files into x and y data
for i in DataFile:
    c = i[0:-1]
    Data.append(c)
for i in range(len(Data)):
    if i % 2 == 0:
        XData.append(Data[i])
    else:
        YData.append(Data[i])
XData1 = []
YData1 = []
for i in range(len(XData)):
    N = XData[i]
    RemovedX = N[-1]
    RemovedX = int(RemovedX)
    XData1.append(RemovedX)
for i in range(len(YData)):
    N = YData[i]
    RemovedY = N[-1]
    RemovedY = int(RemovedY)
    YData1.append(RemovedY)



# This finds the corresponding Y variable in a list when inputting a X variable
count = 0
while count == 0:
    X = int(input("Please enter a value of X variable to find corresponding Y variable or a negative # to cancel: "))
    if X < 0:
        count += 1
    else:
        if X in XData1:
            index = XData1.index(X)
            print("The corresponding y variable is: ", YData1[index])
        else:
            print("The variable is not present in the data file.")
DataFile.close()


