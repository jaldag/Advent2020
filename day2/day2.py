import re

file = open("data.txt", "r")

part1count, part2count = 0, 0

for x in file :
	groups = re.search("^(\d+)-(\d+) (.): (.+)$", x)
	low = int(groups.group(1))
	high = int(groups.group(2))
	char = groups.group(3)
	password = groups.group(4)

	if password.count(char) >= low and password.count(char) <= high :
		part1count += 1
	if (password[low-1] == char) ^ (password[high-1] == char) :
		part2count += 1

print "Part 1: " + str(part1count)
print "Part 2: " + str(part2count)