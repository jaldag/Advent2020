file = open("data.txt", "r")

maxVal = 0
rows = {}

for x in file :
	x = x.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
	maxVal = max(maxVal, int(x[0:7], 2) * 8 + int(x[7:10], 2))
	if x[0:7] in rows.keys() :
		rows[x[0:7]].add(int(x[7:10], 2))
	else :
		rows[x[0:7]] = {int(x[7:10], 2)}

for row in rows :
	if len(rows[row]) == 7 :
		print "P2: " + str(int(row, 2) * 8 + (28 - sum(rows[row]))) ## 28 = 7*8/2

print "P1: " + str(maxVal)