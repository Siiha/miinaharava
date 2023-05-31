from miina_k import *
from sys import argv
			
k = Kartta(int(argv[1]),int(argv[2]))
u = UI(k,int(argv[1]))
tappio = False
while set(u.miinat) != set(k.miinat):
	valinta = int(input("valinta miinamerkintä ta katso ruutu 0 tai 1: "))
	ruutu = tuple(map(int,input("Anna 0-"+str(int(argv[1])-1)+" koordinaatti muodossa x y: ").split()[::-1]))
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
