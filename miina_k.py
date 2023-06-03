from random import randint
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
class Kartta:
	def __init__(self,s,m):
		self.miinat=[(randint(0,s-1),randint(0,s-1)) for i in range(m)]
		self.ruudut={(i,j): numeroi((i,j),self.miinat,s) if (i,j) not in self.miinat else "M" for i in range(s) for j in range(s)}
class UI:
	def __init__(self,kartta,s):
		self.s = s
		self.miinat = []
		self.katsotut = []
		self.kartta = kartta
	def vuorovaikutus(self,valinta,ruutu):
		self.valinta = valinta
		self.ruutu = ruutu
		if self.valinta:
			self.katsotut.append(self.ruutu)
		else:
			self.miinat.append(self.ruutu)
	def	piirra(self):
		self.kuva = [["X"]*self.s for i in range(self.s)]
		for i in self.katsotut+self.miinat:
			self.kuva[i[0]][i[1]]=str(self.kartta.ruudut[i])
		for i in self.kuva:
			print(i)
	def katso_viereiset(self):
		if numeroi(self.ruutu,self.kartta.miinat,self.s) == 0 or numeroi(self.ruutu,self.kartta.miinat,self.s)==numeroi(self.ruutu,self.miinat,self.s):
			l = [i for i in set(viereiset(self.ruutu,self.s)) if i not in self.miinat]
			for j in l:
				if numeroi(j,self.kartta.miinat,self.s)==0 or numeroi(j,self.kartta.miinat,self.s)==numeroi(j,self.miinat,self.s)!=0:
					l+=[i for i in set(viereiset(j,self.s)) if i not in l and i not in self.miinat]
			self.katsotut+=l
