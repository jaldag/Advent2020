file = [int(l.strip()) for l in open("data.txt")]
file.sort()
file.append(max(file) + 3)
file.insert(0, 0)

counts = [0] * 3

for x in range(len(file)-1) :
	counts[file[x+1] - file[x] - 1] += 1
print "P1: " + str(counts[0] * counts[2])

def recurseCombinations(x) :
	if x <= 1 :
		return 0
	if x == 2 :
		return 1
	return recurseCombinations(x-1) + recurseCombinations(x-2) + 1

p2 = 1
x = 0
while x < len(file) - 1 :
	inARow = 1
	for y in range(x+1, len(file)) :
		if y - x == file[y] - file[x] :
			inARow += 1
		else :
			break
	p2 *= max(recurseCombinations(inARow), 1)
	x += inARow
print "P2: " + str(p2)

combos = [1] + [0]*file[-1]
for i in file[1:]:
	combos[i] = combos[i-3] + combos[i-2] + combos[i-1]
print "P2: " + str(combos[-1])