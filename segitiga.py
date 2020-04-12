#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 1
#Tanggal : 08-04-2020

alas, tinggi = map(int, input().split())

if (alas <= 0) or (tinggi <= 0):
	print("Alas dan tinggi harus > 0")
else:
	luas = round(0.5 * alas * tinggi)

	print(luas)
