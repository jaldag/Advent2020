import re

def checkRange(val, length, minimum, maximum) :
	if val != '' :
		num = int(val)
		if len(val) == length and minimum <= num <= maximum :
			return True
	return False

class Passport :
	byr, iyr, eyr, hgt, hcl, ecl, pid, cid = '', '', '', '', '', '', '', ''

	def isValid(self) :
		self.__dict__.pop('cid', None)
		return len(self.__dict__.items()) == 7

file = open("data2.txt", "r")

passports = []
partialPassport = Passport()

for x in file :
	if len(x) == 1 :
		passports.append(partialPassport)
		partialPassport = Passport()
	for y in re.findall('(...):([^ ]+)\s', x) :
		setattr(partialPassport, y[0], y[1])
passports.append(partialPassport)

count = 0
countValid = 0
validColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for passport in passports :
	if passport.isValid() :
		count += 1
		if checkRange(passport.byr, 4, 1920, 2002) :
			if checkRange(passport.iyr, 4, 2010, 2020) :
				if checkRange(passport.eyr, 4, 2020, 2030) :
					height = re.search('^(\d+)(cm|in)$', passport.hgt)
					if height != None :
						if height.group(2) == 'cm' and checkRange(height.group(1), 3, 150, 193) or height.group(2) == 'in' and checkRange(height.group(1), 2, 59, 76) :
							if re.search('^#[0-9a-f]{6}$', passport.hcl) :
								if validColors.count(passport.ecl) > 0 :
									if re.search('^\d{9}$', passport.pid) :
										countValid += 1

print "P1: " + str(count)
print "P2: " + str(countValid)