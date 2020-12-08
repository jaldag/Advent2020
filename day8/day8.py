file = open("data.txt", "r").readlines()

size = len(file)

def traverse(file, flip) :
	vals = set()
	x, acc = 0, 0
	while True :
		if x in vals :
			if flip == -1 :
				break #Part 1
			else :
 				return 0 #Part 2
		vals.add(x)
		if x >= len(file) :
			return acc
		op = file[x][0:3]
		if flip == x : #Part 2
			if op == 'jmp' :
				op = 'nop'
			elif op == 'nop' :
				op = 'jmp'
		if op == 'acc' :
			acc += int(file[x].strip().split(' ')[1])
			x += 1
		elif op == 'jmp' :
			x += int(file[x].strip().split(' ')[1])
		else :
			x += 1

	return acc



print "P1: " + str(traverse(file, -1))
for x in range(len(file)) :
	val = traverse(file, x)
	if val != 0 :
		print "P2: " + str(val)
		break