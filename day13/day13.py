file = open("data.txt", "r").readlines()

start = int(file[0])

busses = file[1].split(',')
pairs = []

minDistance = start
p1 = -1
multiplier = 1

for i, bus in enumerate(busses) :
	if bus == 'x' :
		continue
	pairs.append((int(bus) - i, int(bus)))
	multiplier *= int(bus)
	if minDistance > int(bus) - (start % int(bus)) :
		minDistance = int(bus) - (start % int(bus))
		p1 = int(bus)

print "P1: " + str(p1 * minDistance)

p2 = 0
for pair in pairs :
	val = multiplier / pair[1]
	p2 += pair[0] * val * pow(val, pair[1]-2, pair[1])
	p2 %= multiplier
print "P2: " + str(p2)