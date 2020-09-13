# By submitting this assignment, all team members agree to the following:
# # “Aggies do not lie, cheat, or steal, or tolerate those who do”
# # “I have not given or received any unauthorized aid on this assignment”
# #
# # Names: Abdullah Ahmad
# # Raymond Mee
# # Ricky Lee
# # Eric Stevelman
# # Section: 518
# # Assignment: Lab 7 - ACT 1
# Date: 15/10/18

import numpy
list_widgets = []
inc = 0
dec = 0
num_widgets = 1
total = 0
while num_widgets > 0:
   num_widgets = int(input("Enter number of widgets: "))
   if(num_widgets < 0):
    break
   list_widgets.append(num_widgets)
print(list_widgets)
for g in range(1, len(list_widgets)+1):
    for i in range(len(list_widgets)- g):
        if (list_widgets[i] < list_widgets[i+g]):
            inc += 1
        elif(list_widgets[i] > list_widgets[i + g]):
            dec += 1
        print("")
    print(g, "day interval ",(format(inc/(len(list_widgets) - g) * 100), "were increasing"))
    print("and",(format((dec/(len(list_widgets) - g))* 100), "were decreasing"))
    inc = 0
    dec = 0


