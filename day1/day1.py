file = open("data.txt", "r")

values = []

for x in file :
	values.append(int(x))

for x in range(len(values)) :
	for y in range(x + 1, len(values)) :
		if values[x] + values[y] == 2020 :
			print "Part 1: " + str(values[x] * values[y])
		for z in range(y + 1, len(values)) :
			if values[x] + values[y] + values[z] == 2020 :
				print "Part 2: " + str(values[x] * values[y] * values[z])