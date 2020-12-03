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
		idx[i] += incrementor[i]
		if idx[i] >= len(x) :
			idx[i] = idx[i] - len(x)
print trees
print numpy.prod(trees)