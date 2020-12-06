file = open("data.txt", "r")

curGroup, curGroup2 = set(), set()
count, count2 = 0, 0
newGroup = True

for x in file :
	x = x.strip()
	if len(x) == 0 :
		count += len(curGroup)
		count2 += len(curGroup2)
		curGroup = set()
		newGroup = True
	else :
		newLine = set()
		for c in x :
			curGroup.add(c)
			newLine.add(c)
		if newGroup :
			newGroup, curGroup2 = False, newLine
		else :
			curGroup2 = curGroup2.intersection(newLine)

count += len(curGroup)
count2 += len(curGroup2)

print "P1: " + str(count)
print "P2: " + str(count2)