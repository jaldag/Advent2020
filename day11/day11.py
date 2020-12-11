import copy

file = [list(l.strip())for l in open("data.txt")]

currFile = copy.deepcopy(file)
nextFile = copy.deepcopy(currFile)

def isOccupied(currFile, x, y, deltaX, deltaY) :
	while x + deltaX >= 0 and x + deltaX <= len(currFile)- 1 and y + deltaY >= 0 and y + deltaY <= len(currFile[y]) -1  :
		x += deltaX
		y += deltaY
		if currFile[x][y] == '.' : #Uncomment for Part 2, comment for Part 1
			continue
		return currFile[x][y] == '#'

changed = False

while True :
	for x in range(len(file)) :
		for y in range(len(file[0])) :
			if currFile[x][y] == '.' :
				continue
			seatsAdjacent = 0
			if isOccupied(currFile, x, y, 1, 0) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, 1, 1) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, 1, -1) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, 0, 1) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, 0, -1) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, -1, 0) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, -1, 1) :
				seatsAdjacent += 1
			if isOccupied(currFile, x, y, -1, -1) :
				seatsAdjacent += 1
			if seatsAdjacent == 0 and currFile[x][y] == 'L' :
				nextFile[x][y] = '#'
				changed = True
			elif seatsAdjacent >= 5 and currFile[x][y] == '#' : #4 for Part 1, 5 for Part 2
				nextFile[x][y] = 'L'
				changed = True
	if not changed :
		break
	changed = False
	currFile = copy.deepcopy(nextFile)
val = 0
for x in range(len(file)) :
	val += currFile[x].count('#')
print val