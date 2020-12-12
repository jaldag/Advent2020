import math

file = open("data.txt", "r").readlines()

facing = 1 #N, E, S, W = 0, 1, 2, 3
coords = [0, 0] #, x, y coords

def rotate(point, angle):
    px, py = point

    qx = math.cos(math.radians(angle)) * px - math.sin(math.radians(angle)) * py
    qy = math.sin(math.radians(angle)) * px + math.cos(math.radians(angle)) * py
    return [qx, qy]

for x in file :
	cmd = x[0]
	val = int(x[1:])

	if cmd == 'R' :
		facing = (facing + val/90) % 4
	elif cmd == 'L' :
		facing = (facing - val/90) % 4
	elif cmd == 'N' or cmd == 'F' and facing == 0 :
		coords[1] += val
	elif cmd == 'E' or cmd == 'F' and facing == 1 :
		coords[0] += val
	elif cmd =='S' or cmd == 'F' and facing == 2:
		coords[1] -= val
	elif cmd == 'W' or cmd == 'F' and facing == 3 :
		coords[0] -= val

print "P1 : " + str(abs(coords[0]) + abs(coords[1]))

coords = [0, 0]
waypoint = [10, 1]

for x in file :
	cmd = x[0]
	val = int(x[1:])

	if cmd == 'R' :
		waypoint = rotate(waypoint, val * -1)
	elif cmd == 'L' :
		waypoint = rotate(waypoint, val)
	elif cmd == 'F' :
		coords[0] += waypoint[0] * val
		coords[1] += waypoint[1] * val
	elif cmd == 'N' :
		waypoint[1] += val
	elif cmd == 'E' :
		waypoint[0] += val
	elif cmd =='S' :
		waypoint[1] -= val
	elif cmd == 'W' :
		waypoint[0] -= val

print "P2 : " + str(abs(coords[0]) + abs(coords[1]))