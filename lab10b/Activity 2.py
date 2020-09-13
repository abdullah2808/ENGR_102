# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB10b-Activity 2
# Date: 3 11 2018

import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.dates

date = []
days = []
avgtemp = []
avgpres = []
precip = []
dewavg = []
temphi = []
templow = []
weatherdata = open("WeatherDataWindows.csv", 'r')

# df = Load CSV into a dataframe (google pandas read csv)
# Create month dataframes
#   jan = df[df['Date'].str.match('1/*')]
#   feb = df[df['Date'].str.match('2/*')]
#   ...
# Get means by calling .mean() function
#   jan["Temp Avg"].mean()
#   feb["Temp Avg"].mean()
#   ...


plots = csv.reader(weatherdata, delimiter=',')
for row in plots:
    avgtemp.append((row[2]))
    avgpres.append((row[11]))
    precip.append((row[13]))
    dewavg.append((row[5]))
    temphi.append((row[1]))
    templow.append((row[5]))
    date.append((row[0]))
avgtemp.remove(avgtemp[0])
avgpres.remove(avgpres[0])
precip.remove(precip[0])
dewavg.remove(dewavg[0])
temphi.remove(temphi[0])
templow.remove(templow[0])
date.remove(date[0])

for i in range(1095):
    avgpres[i] = float(avgpres[i])
    avgtemp[i] = float(avgtemp[i])
    precip[i] = float(precip[i])
    dewavg[i] = float(dewavg[i])
    days += [i]
print(avgtemp)
#line graph of Temp and Pressure
plt.figure(1)
plt.plot(days, avgtemp,"b", label="Average Temperature")
plt.xlabel("Days")
plt.axis([0, 1100, 25, 100])
plt.ylabel("Average Temperature")
#axis Switch
plt.twinx()
plt.plot(days, avgpres, "r--", label="Average Pressure")
plt.plot(np.nan, 'b', label = 'Average Temperature ')
plt.ylabel("Average Pressure")
plt.title("Average Pressure and Temperature over Days")
plt.legend()


#Histogram
plt.figure(2)
bins = np.arange(0 ,4,.25)

plt.hist(precip, bins)
plt.xlabel("Precipitation (in)")
plt.ylabel("Days")
plt.title("Days of Precipitation")


#scatter
plt.figure(3)
plt.scatter(avgtemp, dewavg)
plt.ylabel("Average Dew Point")
plt.xlabel('Average Temperature')
plt.title("Dew Point Average vs Temperature Average")


#bar chart month
# seperate lists to hold the avg temperature data of each month
jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec = [], [], [], [], [], [], [], [], [], [], [], []

data = open("WeatherDataWindows.csv", "r")

# Looking at the date on each line tells the computer which list to sort the data into
for s in data:
    strung = s.split(",")
    month = strung[0].split("/")
    if month[0] == '1':
        jan.append(int(strung[2]))
    elif month[0] == '2':
        feb.append(int(strung[2]))
    elif month[0] == '3':
        mar.append(int(strung[2]))
    elif month[0] == '4':
        apr.append(int(strung[2]))
    elif month[0] == '5':
        may.append(int(strung[2]))
    elif month[0] == '6':
        jun.append(int(strung[2]))
    elif month[0] == '7':
        jul.append(int(strung[2]))
    elif month[0] == '8':
        aug.append(int(strung[2]))
    elif month[0] == '9':
        sep.append(int(strung[2]))
    elif month[0] == '10':
        octo.append(int(strung[2]))
    elif month[0] == '11':
        nov.append(int(strung[2]))
    elif month[0] == '12':
        dec.append(int(strung[2]))

n_groups = 12  # specifies the number of bins the bar graph will have in total

# calculates the mean value of each month's temp
means_Temp = ((sum(jan) / len(jan)), (sum(feb) / len(feb)), (sum(mar) / len(mar)), (sum(apr) / len(apr)),
              (sum(may) / len(may)), (sum(jun) / len(jun)), (sum(jul) / len(jul)), (sum(aug) / len(aug)),
              (sum(sep) / len(sep)), (sum(octo) / len(octo)), (sum(nov) / len(nov)), (sum(dec) / len(dec)))

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

# calculates the amount the error line should go into the bar by subtracting the lowest value by the mean of each month
lower_error = ((sum(jan) / len(jan)) - min(jan), (sum(feb) / len(feb)) - min(feb), (sum(mar) / len(mar)) - min(mar),
               (sum(apr) / len(apr)) - min(apr), (sum(may) / len(may)) - min(may), (sum(jun) / len(jun)) - min(jun),
               (sum(jul) / len(jul)) - min(jul), (sum(aug) / len(aug)) - min(aug), (sum(sep) / len(sep)) - min(sep),
               (sum(octo) / len(octo)) - min(octo), (sum(nov) / len(nov)) - min(nov), (sum(dec) / len(dec)) - min(dec))

# calculates the amount the error line should go above the bar
# by subtracting the mean of each month by the highest value
upper_error = (max(jan) - (sum(jan) / len(jan)), max(feb) - (sum(feb) / len(feb)), max(mar) - (sum(mar) / len(mar)),
               max(apr) - (sum(apr) / len(apr)), max(may) - (sum(may) / len(may)), max(jun) - (sum(jun) / len(jun)),
               max(jul) - (sum(jul) / len(jul)), max(aug) - (sum(aug) / len(aug)), max(sep) - (sum(sep) / len(sep)),
               max(octo) - (sum(octo) / len(octo)), max(nov) - (sum(nov) / len(nov)), max(dec) - (sum(nov) / len(nov)))

asymmetric_error = [lower_error, upper_error]

rects1 = ax.bar(index, means_Temp, bar_width,
                alpha=opacity, color='g',
                yerr=asymmetric_error, error_kw=error_config,
                label='Mean Value')

ax.set_xlabel('Months')
ax.set_ylabel('Temperature')
ax.set_title('Average Temperatures over Months')
ax.set_xticks(index + bar_width / 6)
ax.set_xticklabels(('Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.',
                    'Nov.', 'Dec.'))
ax.legend()

fig.tight_layout()
plt.show()


