from miina_k import *
from collections import deque
class AI:
	def __init__(self,ui,s,kartta):
		self.ui = ui
		self.s = s
		self.kartta = kartta
		self.mahdolliset = deque()
	def kay_lapi(self):
		a = self.ui.katsotut[:]
		for i in a:
			self.ui.vuorovaikutus(1,i)
			self.ui.katso_viereiset()
	def merkitse(self):
		a = self.ui.katsotut[:]
		for i in a:
			l = list(set([j for j in viereiset(i,self.s) if self.ui.kuva[j[0]][j[1]]=="X" or self.ui.kuva[j[0]][j[1]]=="M"]))
			if len(l) == self.kartta.ruudut[i]:
				self.ui.miinat+=l
			elif self.kartta.ruudut[i]!=0:
				self.mahdolliset+=l
	def ma_kay_lapi():
		pass
	def pelaa(self):
		self.kay_lapi()
		self.ui.piirra()
		self.merkitse()
		for i in self.kartta.ruudut.keys():
			if i not in self.ui.miinat and i not in self.mahdolliset:
				self.ui.vuorovaikutus(1,i)
				break
		self.ui.piirra()
k = Kartta(10,10)
u = UI(k,10)
ai = AI(u,10,k)
while set(u.miinat)!=set(k.miinat):
	ai.pelaa()
	print()
	for i in u.kuva:
		print(i)
	if pum(u.katsotut,k.miinat):
		print("PUM!!")
		break
