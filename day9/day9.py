file = [int(l.strip()) for l in open("data.txt")]

idx = 25
p1 = 0

while True :
	for x in range(idx - 25, idx) :
		if file[idx] - file[x] in file[x+1:idx] :
			idx += 1
			break
	else :
		p1 = file[idx]
		break
print "P1: " + str(p1)

window = []
for x in file:
	if sum(window) == p1 :
		break
	window.append(x)
	while sum(window) > p1 :
		window.pop(0)
print "P2: " + str(min(window) + max(window))