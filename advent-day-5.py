import fileinput

goodWords = 0

for line in fileinput.input():
	vowels = 0
	doubles = 0
	badStrings = 0
	previousChar = ' '
	for char in line:
		if char is 'a' or char is 'e' or char is 'i' or char is 'o' or char is 'u':
			vowels = vowels + 1
		if char is 'd':
			if previousChar is 'a' or previousChar is 'c':
				break
		if char is 'q':
			if previousChar is 'p':
				break
		if char is 'y':
			if previousChar is 'x':
				break
		if char is previousChar:
			doubles = doubles + 1
		previousChar = char
		if vowels >= 3 and doubles >= 1:
			goodWords = goodWords + 1
			break

print(goodWords)