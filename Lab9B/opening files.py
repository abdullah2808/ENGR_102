a = open("random_ints.txt", 'r')
listtotals = []
for i in a:
    lnum = i.split()
    for j in range(len(lnum)):
        lnum[j] = int(lnum[j])
    listtotals.append(sum(lnum))
print(listtotals)
diff = 0
listdiffs = []
num = int(input("Please enter a number: "))
for z in range(len(listtotals)):
    diff = abs(listtotals[z] - num)
    listdiffs.append(diff)
smallestdiff = min(listdiffs)
print("Row #",(listdiffs.index(smallestdiff)+1),"is the closest to your number")
a.close()

b = open("doi.txt", "r")
for d in b:
    print(d)
    
