#Nama : Faishal Zharfan

n = int(input(""))
kesegaran = list(map(int,input("").split()[:n]))
kegiatan = int(input(""))
maks  = [0 for i in range(kegiatan)]
jumlah = [0 for i in range(kegiatan)]
hasil = kegiatan

while kegiatan >= 1:
	pilihan = list(map(int,input("").split()))
	if pilihan[0] == 1 :
		kesegaran[pilihan[1]-1] =  kesegaran[pilihan[1]-1] + 1
	elif pilihan[0] == 2 :
		for i in range(pilihan[1]-1, pilihan[2]):
			if maks[6-kegiatan] <= kesegaran[i]:
				maks[6-kegiatan] = kesegaran[i]
				jumlah[6-kegiatan] = jumlah[6-kegiatan] + kesegaran[i]
		#print(maks[6-kegiatan],jumlah[6-kegiatan])
	kegiatan = kegiatan - 1

for i in range(hasil):
	if maks[i] > 0 and jumlah[i] > 0:
		print(maks[i], jumlah[i])
	


