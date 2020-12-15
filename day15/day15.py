file = open("data.txt", "r").readlines()

nums = [int(x) for x in file[0].split(',')]

idx = 0
cache = dict()

for i, num in enumerate(nums) :
	if i < len(nums) - 1 :
		cache[num] = i

while len(nums) < 30000000 : #P1 = 2020, P2 = 30000000
	prev = nums[-1]
	prev2 = cache.get(prev, -1)
	cache[prev] = len(nums) - 1
	nxt = 0
	if prev2 > -1 :
		nxt = len(nums) - 1 - prev2
	nums.append(nxt)
print nums[-1]