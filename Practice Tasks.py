from statistics import mean
import random

MarkList = [90, 83, 4, 78, 10]

# print(min(MarkList))
# print(max(MarkList))
# print(mean(MarkList))

TempReading = []
for i in range(5):
    reading = str(input("Enter the temperature reading; "))
    if reading[-1] == "F" or reading[-1] == "f":
        reading = reading[:-1]

        reading = ((float(reading) - 32) * 5) /9

        TempReading.append(reading)

    else:
        reading = reading[:-1]
        TempReading.append(float(reading))

print((TempReading))
print(max(TempReading))
print(min(TempReading))
print(mean(TempReading))
range = max(TempReading) - min(TempReading)
print(range)
