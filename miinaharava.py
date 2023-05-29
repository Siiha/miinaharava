import random
from miina_k import *
s = int(input("Anna kentän sivun pituus: "))
land = [[0 for i in range(s)] for i in range(s)]
m = int(input("Anna haluamasi miinojen määrä (määrä voi olla pienempi, jos miinoille osuu sama sijainti ne lasketaan yhdeksi): "))
# miinat[0][1] 0 on y ja 1 on x
miinat = [(random.randint(0,s-1),random.randint(0,s-1)) for i in range(m)]
for i in miinat:
	land[i[0]][i[1]]="M"
for i in range(s):
	for j in range(s):
		if land[i][j]!="M": land[i][j]=numeroi((i,j),miinat,s)
katsotut = []
merkityt = []
while set(merkityt) != set(miinat):
	valinta = int(input("valinta miinamerkintä ta katso ruutu 0 tai 1: "))
	syote = tuple(map(int,input("Anna 0-"+str(s-1)+" koordinaatti muodossa y x: ").split()))
	if valinta:
		if syote not in katsotut:
			katsotut.append(syote)
	else:
		merkityt.append(syote)
	kuva = [["X" for i in range(s)] for i in range(s)]
	for i in merkityt:
		kuva[i[0]][i[1]]="M"
	if valinta:
		viimeisin = syote
		if land[viimeisin[0]][viimeisin[1]]==0 or numeroi(viimeisin,merkityt,s) == land[viimeisin[0]][viimeisin[1]]:
			vv = [i for i in set(viereiset(viimeisin,s)) if i not in merkityt]
			for i in vv:
				if land[i[0]][i[1]]==0 or numeroi(i,merkityt,s)==land[i[0]][i[1]]:
					vv+=[j for j in set(viereiset(i,s)) if j not in vv and j not in merkityt]
				
			katsotut += vv
	
	for i in katsotut:
		kuva[i[0]][i[1]]=str(land[i[0]][i[1]])
	for i in kuva:
		print(i)
	if pum(katsotut,miinat):
		print("Pum")
		break
