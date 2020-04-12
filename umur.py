#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 4
#Tanggal : 01-04-2020

umur = [int(input('')) for i in range(20)]
i = 0

tertinggi = 0
terendah = 999

for i in range(20):
	if tertinggi <= umur[i]:
		tertinggi = umur[i]
for i in range(20):
	if terendah >= umur[i]:
		terendah = umur[i]

for i in range(20):
	print('[P' + str(i+1) + ']' + str(umur[i]))

print('Tertinggi = ' + str(tertinggi))
print('Terendah = ' + str(terendah))