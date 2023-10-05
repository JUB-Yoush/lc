def minEatingSpeed(piles,h):
	
	potential_speeds = list(range(1,max(piles)+1))
	l = 0
	r = potential_speeds[-1]
	k = (r+l)//2
	found = False
	while not found:
		current_spd = potential_speeds[k]
		eat_speed = getEatingSpeed(piles,h,current_spd)
		if eat_speed == h:
			return potential_speeds[k]
		if eat_speed > h: # rm bottom half
			l = k
			k = (r+l)//2
		elif eat_speed < h: #rm top half
			r = k
			k = (r+l)//2



def getEatingSpeed(piles,h,spd):
	hours = 0
	for pile in piles:
		count = pile 
		while count > 0:
			count -= spd
			hours += 1
	return hours
	

print(minEatingSpeed([3,6,7,11],8)) 