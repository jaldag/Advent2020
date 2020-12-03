file = open("data.txt", "r")

idx = [0] * 5
trees = [0] * 5
slope = [1, 3, 5, 7, .5]

for line in file :
	line = line.strip()
	for i in range(len(idx)) :
		if line[int(idx[i])] == '#' and idx[i] == int(idx[i]):
			trees[i] += 1
		idx[i] = (idx[i] + slope[i]) % len(line)

print "P1: " + str(trees[1])
print "P2: " + str(reduce(lambda a, b: a*b, trees))