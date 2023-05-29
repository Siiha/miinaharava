def viereiset(sijainti,s):
	x0, y0 = sijainti
	a = (1, 0, -1)
	for dx in a:
		for dy in a:
			if dx == 0 and dy == 0:
				continue
			x = x0 + dx
			y = y0 + dy
			if 0 <= x < s and 0 <= y < s:
				yield (x, y)
def numeroi(sijainti,miinat,s):
	c = 0
	v = set(viereiset(sijainti,s))
	for i in set(miinat):
		c += i in v
	return c
pum = lambda katsotut,miinat: set(katsotut) & set(miinat)
