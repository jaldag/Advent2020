import re

file = open("data.txt", "r").readlines()

low = 25
high = 970

ranges = list()
possible = list()

mine = [83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71]

for x in range(20) :
	ranges.append([0, 0, 0, 0])
	possible.append({y for y in range(20)})

	groups = re.search('^.*: (\d+)-(\d+) or (\d+)-(\d+).*$', file[x])
	ranges[x][0] = int(groups.group(1))
	ranges[x][1] = int(groups.group(2))
	ranges[x][2] = int(groups.group(3))
	ranges[x][3] = int(groups.group(4))

p1 = 0
for x in range(25, len(file)) :
	nums = [int(y) for y in file[x].strip().split(',')]
	bad = False
	for num in nums :
		if num < low or num > high :
			p1 += num
			bad = True
	if not bad :
		for y in range(20) :
			for z in range(20) :
				if nums[y] < ranges[z][0] or nums[y] > ranges[z][1] and nums[y] < ranges[z][2] or nums[y] > ranges[z][3] :
					possible[y].discard(z)
print "P1: " + str(p1)
trim = True
while trim :
	trim = False
	for set_ in possible :
		if len(set_) == 1 :
			for set_2 in possible :
				if set_ != set_2 :
					set_2.discard(list(set_)[0])
		else :
			trim = True
p2 = 1
for x in range(20) :
	for y in range(6) :
		if y in possible[x] :
			p2 *= mine[x]
print "P2: " + str(p2)