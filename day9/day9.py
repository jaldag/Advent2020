#file = open("data.txt", "r").readlines()
file = [int(l.strip()) for l in open("data.txt")]

preamble = 25
nums = list()

for x in range(preamble) :
	nums.append(file[x])

idx = preamble
p1 = 0

while True :
	brk = False
	for x in range(idx - preamble, len(nums) - 1) :
		for y in range(x + 1, len(nums)) :
			if file[x] + file[y] == file[idx] :
				idx += 1
				nums.append(file[idx])
				brk = True
				break
		if brk :
			break
	if brk == False :
		p1 = file[idx]
		break
	else :
		brk = False

print "P1: " + str(p1)

for x in range (idx - 1) :
	brk = False
	for y in range(x + 1, idx) :
		val = 0
		for z in range(x, y + 1) :
			val += file[z]
		if val == p1 :
			low = float('inf')
			high = 0
			for v in range(x, y+1) :
				low = min(low, file[v])
				high = max(high, file[v])
			print "P2: " + str(low + high)
			brk = True
		if val > p1 :
			break
	if brk :
		break