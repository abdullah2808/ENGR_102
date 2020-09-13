b = open("doi.txt", "r")
counta = 0
countthey = 0
for d in b:
    print(d)
    s = d.split()
    print(s)
    if "a" in d or "A" in d:
        counta += 1
    if "they" in d:
        countthey += 1
print(counta)
print(countthey)
