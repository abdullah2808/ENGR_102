import random

print(random.randint(1,9))

sum = []
total = 0
for i in range(1,101):
    sum += [i]
for i in sum:
    total += i
print(sum)
print(total)

print ("------------")
print ('Fibonacci')

a = 1
b = 1
fib = 0
x = []
for i in range (50):
    a = b
    b = fib
    fib = a + b
    x += [fib]
print (x)

print("-----------------")
print("7")
negcheck = 0
n1 = int(input("Please enter num"))
n2 = int(input("Please enter num"))
dividors = []
while negcheck == 0:
    if n1 > n2:
        for i in range(2, n1):
            if (n1 % i == 0) and (n2 % i == 0):
                dividors += [i]
                negcheck += 1
    else:
        for i in range(2, n2):
            if (n1 % i == 0) and (n2 % i == 0):

                negcheck += 1
                dividors += [i]
largets = max(dividors)
print(largets)

print("-factorial-")

n = int(input("enter a number"))
fact = 1
fact2 = 0
for i in range(n):
    fact = fact * n
    n = n - 1
print(fact)

