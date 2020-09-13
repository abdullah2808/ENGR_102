A = [10, 87, 101, 1, 43, 7, 8, 15, 123, 95, 77, 10]
AA = []
B = ['cable', 'engr102', 'zachry', 'INSTRUCTS', "in", "students", "with the", "best"]
C = [[1, 2, 3], 'proton', 'electron', [['A', 'B'],[1, 2, 3, 4], 5, 'cable'], ['a', 'b', 'c', 'd', 'e'], 'f']
sum = 0


newA = []
while A:
    minimum = A[0]
    for i in A:
        if i > minimum:
            minimum = i
    newA.append(minimum)
    A.remove(minimum)
A = newA
print (A)
avgchar = 0

for i in B:
    avgchar += len(i)
avgchar = avgchar/len(B)
print (avgchar)


for i in A:
    if i % 2 == 0:
        continue
    else:
        AA += [i]
print (AA)

for i in A:
    sum += i

avg = sum/(len(A))
print (avg)

A.sort()
E = len(A)/2
E = int(E)
print (A[E])


runner = 0





print (A)