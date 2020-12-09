file = open("data.txt", "r").readlines()

preamble = 25
nums = list()

for x in range(preamble) :
	nums.append(int(file[x].strip()))

idx = preamble
p1 = 0

while True :
	brk = False
	for x in range(idx - preamble, len(nums) - 1) :
		for y in range(x + 1, len(nums)) :
			if int(file[x].strip()) + int(file[y].strip()) == int(file[idx].strip()) :
				idx += 1
				nums.append(int(file[idx].strip()))
				brk = True
				break
		if brk :
			break
	if brk == False :
		p1 = int(file[idx].strip())
		break
	else :
		brk = False

print "P1: " + str(p1)

for x in range (idx - 1) :
	brk = False
	for y in range(x + 1, idx) :
		val = 0
		for z in range(x, y + 1) :
			val += int(file[z].strip())
		if val == p1 :
			low = 99999999999999
			high = 0
			for v in range(x, y+1) :
				low = min(low, int(file[v].strip()))
				high = max(high, int(file[v].strip()))
			print "P2: " + str(low + high)
			brk = True
		if val > p1 :
			break
	if brk :
		break