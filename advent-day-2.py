import fileinput

length = 0
width = 0
height = 0
totalFeet = 0

for line in fileinput.input():
    splitString = line.split('x')
    length = int(splitString[0]) * int(splitString[1])
    width = int(splitString[1]) * int(splitString[2])
    height = int(splitString[0]) * int(splitString[2])
    minimum = min(length, width, height)
    totalFeet = totalFeet + (2*length + 2*width + 2*height) + minimum

print(totalFeet)