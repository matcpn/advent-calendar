import fileinput

length = 0
width = 0
height = 0
totalFeet = 0

for line in fileinput.input():
    splitString = line.split('x')
    length = int(splitString[0])
    width = int(splitString[1])
    height = int(splitString[2])
    minimum = min(length, width, height)
    minimum2 = 0
    if minimum is length:
        minimum2 = min(width, height)
    if minimum is width:
        minimum2 = min(length, height)
    if minimum is height:
        minimum2 = min(width, length)
    totalFeet = totalFeet + (length * width * height) + 2*minimum + 2*minimum2

print(totalFeet)