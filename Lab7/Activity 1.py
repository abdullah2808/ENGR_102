


production = []
days = int(input('Please enter amount of days: '))
posnegcheck = 0
for i in range(days):
    production += [int(input("Please enter a production value: "))]
for n in range(1,days):
    print("This is n", n)
    posnegcheck = 0
    counter = 0
    count2 = 0
    for z in range(0,days,n):
        print(production[n-1])
        print(production[n])
        print(production[n] - production[n-1])
        posnegcheck = (production[n] - production[n-1])
        if posnegcheck > 0:
            counter += 1
            count2 += n
        elif posnegcheck < 0:
            counter -= 1
            count2 += n
        if count2 >= days:
            print(counter)
            print(count2)
            print("For", n,"day intervals", (counter/days*100), "were increasing and", (100-(days/counter*100)), "were decreasing")





