CelDataFile = open('Celsius.dat', 'r')
CelData = []
FarDataFile = open('Fahrenheit.data', 'w')
for i in CelDataFile: # puts celsius data in a list
    i = int(i)
    CelData.append(i)
for i in range(len(CelData)): # converts to F and writes to file
    Far = ((CelData[i] * 9/5) + 32)
    Far = str(Far)
    FarDataFile.write(Far + '\n')
CelDataFile.close()
FarDataFile.close()