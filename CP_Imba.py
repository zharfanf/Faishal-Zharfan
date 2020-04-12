#Nama : Faishal Zharfan


i= 0
banyak = int(input(''))
barisan = list(map(int,input("").split()[:banyak]))
ngerti = [0 for i in range(banyak)]

for i in range(banyak):
	if i > 0:
		for j in range(i):
			if barisan[i] > barisan[j]:
				ngerti[i] = ngerti[i] + 1


for i in range(banyak):
	print(ngerti[i], end=' ')

