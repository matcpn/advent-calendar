text = 'INPUT'

n = 0
for s in text:
    for i in range(0, len(s)-2):
        if s[i] == s[i+2]:
            break
        else:
            continue

    for i in range(0, len(s)-1):
        if s.count(s[i] + s[i+1]) > 1:
            n += 1
            break
        else:
            continue

print(n)