from miina_k import *
from random import randint
from sys import argv
s = int(argv[1])
m = int(argv[2])
class Kartta:
	def __init__(self):
		self.miinat=[(randint(0,s-1),randint(0,s-1)) for i in range(m)]
		self.ruudut={(i,j): numeroi((i,j),self.miinat,s) if (i,j) not in self.miinat else "M" for i in range(s) for j in range(s)}
class UI:
	def __init__(self,kartta):
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
		self.kuva = [["X"]*s for i in range(s)]
		for i in self.katsotut+self.miinat:
			self.kuva[i[0]][i[1]]=str(self.kartta.ruudut[i])
		for i in self.kuva:
			print(i)
	def katso_viereiset(self):
		if numeroi(self.ruutu,self.kartta.miinat,s) == 0 or numeroi(self.ruutu,self.kartta.miinat,s)==numeroi(self.ruutu,self.miinat,s):
			l = [i for i in set(viereiset(self.ruutu,s)) if i not in self.miinat]
			for j in l:
				if numeroi(j,self.kartta.miinat,s)==0 or numeroi(j,self.kartta.miinat,s)==numeroi(j,self.miinat,s)!=0:
					l+=[i for i in set(viereiset(j,s)) if i not in l and i not in self.miinat]
			self.katsotut+=l			
k = Kartta()
u = UI(k)
tappio = False
while set(u.miinat) != set(k.miinat):
	valinta = int(input("valinta miinamerkintä ta katso ruutu 0 tai 1: "))
	ruutu = tuple(map(int,input("Anna 0-"+str(s-1)+" koordinaatti muodossa x y: ").split()[::-1]))
	u.vuorovaikutus(valinta,ruutu)
	if u.valinta:
		u.katso_viereiset()
	u.piirra()
	if pum(u.katsotut,k.miinat):
		tappio = True
		break
if tappio:
	print("PUM!!")
else:
	print("Hyvää työtä :D")
