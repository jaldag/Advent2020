import re

file = open("data.txt", "r")

def recurseBags(bags, bag) :
	for key in bags :
		for num, color in bags[key] :
			if bag == color :
				p1.add(key)
				recurseBags(bags, key)

def countBags(bags, bag) :
	count = 1
	for num, color in bags[bag] :
		count = count + (int(num) * countBags(bags, color))
	return count

bags = {}
p1 = set()

for x in file :
	vals = re.search('^(\S+ \S+) bags contain (.*)$', x)
	key = vals.group(1)
	containers = re.findall('(\d) (\S+ \S+)', vals.group(2))
	bags[key] = set()
	for container in containers :
		bags[key].add(container)

recurseBags(bags, 'shiny gold')

print "P1: " + str(len(p1))
print "P2: " + str(countBags(bags, 'shiny gold') - 1) #don't include itself