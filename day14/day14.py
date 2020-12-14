import re

file = open("data.txt", "r").readlines()

def maskedVal(mask, val) :
	arr = list(mask)
	binary = str(format(int(val), 'b')).rjust(36, '0')
	for i in reversed(range(36)) :
		if mask[i] == 'X' :
			arr[i] = binary[i]
	return int(''.join(str(e) for e in arr), 2)

def p2Indexes(mask, idx) :
	arr = list(mask)
	binary = str(format(int(idx), 'b')).rjust(36, '0')
	indexes = {}
	for i in reversed(range(36)) :
		if mask[i] == '0' :
			arr[i] = binary[i]
		elif mask[i] == '1' :
			arr[i] = '1'
	indexes = [''.join(str(e) for e in arr)]
	while indexes[0].find('X') > -1 :
		newIndexes = []
		idx = indexes[0].find('X')
		for index in indexes :
			arr = list(index)
			arr2 = list(index)
			arr[idx] = '0'
			arr2[idx] = '1'
			newIndexes.append(''.join(str(e) for e in arr))
			newIndexes.append(''.join(str(e) for e in arr2))
		indexes = newIndexes
	return indexes

mask = None
mem = dict()
mem2 = dict()
for x in file :
	if x[0:4] == 'mask' :
		mask = x.split(' = ')[1].strip()
	else :
		idx = re.search('\\[(\d*)\\]', x).group(1)
		val = re.search('= (\d*)', x).group(1)
		mem[idx] = maskedVal(mask, val)
		for idx2 in p2Indexes(mask, idx) :
			mem2[idx2] = int(val)
print "P1: " + str(sum(mem.values()))
print "P2: " + str(sum(mem2.values()))