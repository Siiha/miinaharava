import random
def viereiset(sijainti,s):
	a = (1,0,-1)
	if sijainti[0]==0:
		if sijainti[1]==0:
			return [(sijainti[0]+1,sijainti[1]),(sijainti[0],sijainti[1]+1),(sijainti[0]+1,sijainti[1]+1)]
		if sijainti[1]==s-1:
			return [(sijainti[0]+1,sijainti[1]),(sijainti[0],sijainti[1]-1),(sijainti[0]+1,sijainti[1]-1)]
		r = [(sijainti[0]+i,sijainti[1]+j) for i in a[:2] for j in a if  (i==0 and j==0) == False]
		return (r)
	if sijainti[0]==s-1:
		if sijainti[1] == 0:
			r = [(sijainti[0]+i,sijainti[1]+j) for i in a[1:] for j in a[:2] if  (i==0 and j==0) == False]
			return r
		if sijainti[1] == s-1:
			r = [(sijainti[0]+i,sijainti[1]+j) for i in a[1:] for j in a[1:] if  (i==0 and j==0) == False]
			return r
		r = [(sijainti[0]+i,sijainti[1]+j) for i in a[1:] for j in a if  (i==0 and j==0) == False]
		return r
	elif sijainti[1]==0:
		r = [(sijainti[0]+i,sijainti[1]+j) for i in a for j in a[:2] if  (i==0 and j==0) == False]
		return r
	elif sijainti[1]==s-1:
		r = [(sijainti[0]+i,sijainti[1]+j) for i in a for j in a[1:] if  (i==0 and j==0) == False]
		return r
	else:
		r = [(sijainti[0]+i,sijainti[1]+j) for i in a for j in a if  (i==0 and j==0) == False]
		return r
def numeroi(sijainti,miinat,s):
	c = 0
	v = viereiset(sijainti,s)
	for i in set(miinat):
		c += i in v
	return c
def pum(katsotut,miinat):
	for i in katsotut:
		if i in miinat:
			return True
	return False
			
s = 5
land = [[0 for i in range(s)] for i in range(s)]
m = s*s//5
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
			vv = [i for i in viereiset(viimeisin,s) if i not in merkityt]
			for i in vv:
				if land[i[0]][i[1]]==0 or numeroi(i,merkityt,s)==land[i[0]][i[1]]:
					vv+=[j for j in viereiset(i,s) if j not in vv and j not in merkityt]
				
			katsotut += vv
	
	for i in katsotut:
		kuva[i[0]][i[1]]=str(land[i[0]][i[1]])
	for i in kuva:
		print(i)
	if pum(katsotut,miinat):
		print("Pum")
		break
