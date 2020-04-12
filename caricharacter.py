#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 6 / Responsi
#Tanggal : 08-04-2020

N = int(input(''))
while (N <= 0 or N > 100):
	print("Masukan salah. Ulangi!")
	N = int(input(''))
arr = [(input())[0] for i in range(N)]
CC = (input())[0]
if (CC == 'S' or CC == 's'):
	i = 0
	Found = False
	while not(Found) and i < N:
		if ord(arr[i]) >= 97 and ord(arr[i]) <= 122:
			Found = True
		else:
			i = i + 1
	if Found == True :
		print(i+1,arr[i])
		print(type(arr[i]))
	else:
		print("Tidak ada huruf kecil")
elif ((CC == 'L' or CC == 'l')):
	i = 0
	Found = False
	while not(Found) and i < N:
		if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
			Found = True
		else:
			i = i + 1	
	if Found == True :
		print(i+1,arr[i])
		print(type(arr[i]))
	else:
		print("Tidak ada huruf besar")
elif ((CC == 'X' or CC == 'x')):
	i = 0
	Found = False
	while not(Found) and i < N:
		if (ord(arr[i]) < 65) or (ord(arr[i]) > 90 and ord(arr[i]) < 97) or (ord(arr[i]) > 122)   :
			Found = True
		else:
			i = i + 1
	if Found == True :
		print(i+1,arr[i])
		print(type(arr[i]))
	else:
		print("Semua huruf")
else :
	print("Tidak diproses")	

