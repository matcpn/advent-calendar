import fileinput

switches = [[0 for x in range(1000)] for x in range(1000)] 

def toggle(int):
	return int + 2

def turnOn(int):
	return int + 1

def turnOff(int):
	if int == 0:
		return 0
	else:
	    return int - 1

for line in fileinput.input():
	words = line.split()
	if words[0] == 'toggle':
		for i in range(int(words[1].split(',')[0]), int(words[3].split(',')[0]) + 1):
			for j in range (int(words[1].split(',')[1]), int(words[3].split(',')[1]) + 1):
				switches[i][j] = toggle(switches[i][j])
	elif words[1] == 'off':
		for i in range(int(words[2].split(',')[0]), int(words[4].split(',')[0]) + 1):
			for j in range (int(words[2].split(',')[1]), int(words[4].split(',')[1]) + 1):
				switches[i][j] = turnOff(switches[i][j])
	elif words[1] == 'on':
		for i in range(int(words[2].split(',')[0]), int(words[4].split(',')[0]) + 1):
			for j in range (int(words[2].split(',')[1]), int(words[4].split(',')[1]) + 1):
				switches[i][j] = turnOn(switches[i][j])

turnedOn = 0

for i in range (1000):
	for j in range(1000):
		turnedOn = turnedOn + switches[i][j]

print(turnedOn)

