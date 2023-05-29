from miina_k import *
import random
rint=random.randint
s = int(input("Anna kentän sivun pituus: "))
m = int(input("Anna haluamasi miinojen määrä (määrä voi olla pienempi, jos miinoille osuu sama sijainti ne lasketaan yhdeksi): "))
miinat = [(rint(0,s-1),rint(0,s-1)) for i in range(m)]
katsotut = []
merkityt = []
while set(merkityt)!=set(miinat):
	kuva = [["X"]*s for i in range(s)]
	valinta = int(input("valinta miinamerkintä ta katso ruutu 0 tai 1: "))
	ruutu = tuple(map(int,input("Anna 0-"+str(s-1)+" koordinaatti muodossa y x: ").split()))
	if valinta:
		katsotut.append(ruutu)
	else:
		merkityt.append(ruutu)
	if valinta:
		if numeroi(ruutu,miinat,s) == 0 or numeroi(ruutu,merkityt,s)==numeroi(ruutu,miinat,s):
			l = [i for i in set(viereiset(ruutu,s)) if i not in merkityt]
			for j in l:
				if numeroi(j,miinat,s)==0 or numeroi(j,miinat,s)==numeroi(j,merkityt,s)!=0:
					l+=[i for i in set(viereiset(j,s)) if i not in l and i not in merkityt]
			katsotut+=l
	for i in katsotut:
		numero_i = numeroi(i,miinat,s)
		kuva[i[0]][i[1]]=str(numero_i)
		if i in miinat: kuva[i[0]][i[1]]="M"
			
	for i in merkityt:
		kuva[i[0]][i[1]]="M"
	for i in kuva:
		print(i)
	if pum(katsotut,miinat):
		print("Pum!!!")
		break
