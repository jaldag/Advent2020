import re

file = open("data.txt", "r")

def recurseBags(bags, bag) :
	for key in bags :
		for vals in bags[key] :
			if bag == vals[1] :
				p1.add(key)
				recurseBags(bags, key)

def countGold(bags, bag) :
	count = 1
	for vals in bags[bag] :
		count = count + (int(vals[0]) * countGold(bags, vals[1]))
	return count

bags = {}
p1 = set()

for x in file :
	vals = re.search('^(\S+ \S+) bags contain (.*)$', x)
	key = vals.group(1)
	values = re.findall('(\d) (\S+ \S+)', vals.group(2))
	bags[key] = set()
	for value in values :
		bags[key].add(value)

recurseBags(bags, 'shiny gold')

print "P1: " + str(len(p1))
print "P2: " + str(countGold(bags, 'shiny gold') - 1) #don't include itself