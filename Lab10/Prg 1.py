import numpy as np

A = np.array([0,10,20,30,40,50,60,70,80,90])
B = np.array([10,30,40,50,70,90])
print(np.setdiff1d(A, B))

C = np.array([10,9,0,13,2,5,3,7,8,1,10,11,12,13,14]).reshape(3,5)
print("Is the array \n", C)
print("The max value is", np.amax(C), "located at", np.nanargmax(C))
print("The min value is", np.amin(C), "located at")

Un = open("un.txt", "r")
doi = open("doi.txt", "r")
words1 = []
words2 = []
for i in Un:
    a = Un.readline()
    a = a.split(" ")

    words1 += (a)
for j in doi:
    b = doi.readline()
    b = b.split(" ")

    words2 += (b)
print(words1)

for word in words1:
    for word2 in words2:
        if word == word2:
            print(word)
        else:
            continue