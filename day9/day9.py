file = [int(l.strip()) for l in open("data.txt")]

idx = 25
p1 = 0

while True :
	brk = True
	for x in range(idx - 25, idx) :
		if file[idx] - file[x] in file[x+1:idx] :
			idx += 1
			brk = False
	if brk:
		p1 = file[idx]
		break
print "P1: " + str(p1)

for x in range(idx - 1) :
	for y in range(x + 1, idx) :
		val = sum(file[x:y+1])
		if val == p1 :
			print "P2: " + str(min(file[x:y+1]) + max(file[x:y+1]))
			quit()
		if val > p1 :
			break