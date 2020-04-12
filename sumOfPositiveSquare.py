#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 3 / Responsi
#Tanggal : 08-04-2020

sum = 0
X = int(input(''))

if (X == -999):
	print(0)
else:
	while (X != -999):
		if (X > 0):
			sum = sum + (X**2)
		X = int(input(''))
	print(sum)