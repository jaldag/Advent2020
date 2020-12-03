import numpy
file = open("data.txt", "r")

idx = [0, 0, 0, 0, 0]
trees = [0, 0, 0, 0, 0]
incrementor = [1, 3, 5, 7, .5]

for x in file :
	x = x.strip()
	for i in range(len(idx)) :
		if x[int(idx[i])] == '#' and idx[i] == int(idx[i]):
			trees[i] += 1
		idx[i] = (idx[i] + incrementor[i]) % len(x)

print "P1: " + str(trees[1])
print "P2: " + str(numpy.prod(trees))