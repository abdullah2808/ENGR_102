# By submitting this assignment, all team members agree to the following:
# # “Aggies do not lie, cheat, or steal, or tolerate those who do”
# # “I have not given or received any unauthorized aid on this assignment”
# #
# # Names: Abdullah Ahmad
# # Raymond Mee
# # Ricky Lee
# # Eric Stevelman
# # Section: 518
# # Assignment: Lab 7 - ACT 2
# Date: 15/10/18



#variables
scores = []
madeit = []
cut = []
golfers = {}
negcheck = 0

# gets scores and golfer names
while negcheck == 0:
    round1 = int(input("Please enter first round score: "))
    if round1 < 0:
        negcheck += 1
        continue
    round2 = int(input("Please enter second round score: "))
    avg = (round1+round2)/2
    user = str(input("Please enter golfer name: "))
    scores += [avg]
    golfers[avg] = user

# sorts list and finds medians
for i in range(len(scores)):
    for j in range(i +1,len(scores)):
        if scores[i] > scores[j]:
            scores[i], scores[j] = scores[j], scores[i]
length = len(scores)
L = int(length / 2)

# finds people who are not cut
for i in range(L+1):
    madeit += [golfers[scores[i]]]
# finds people who are cut
for i in range(L+1,length):
    cut += [golfers[scores[i]]]

print(madeit, "made the cut")
print(cut, "did not make the cut")
