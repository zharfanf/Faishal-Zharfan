#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 4 / Responsi
#Tanggal : 08-04-2020

countT = 0
count = 0
countP = 0
sum = 0
tinggi = int(input(''))

if (tinggi == -999):
	print('Data kosong')
else:
	while (tinggi != -999):
		if (tinggi >= 100) and (tinggi <= 300):
			if (tinggi >= 170):
				countT  = countT + 1
			elif (tinggi <= 150):
				countP = countP + 1
			count = count + 1
			sum = sum + tinggi
		tinggi = int(input(''))
	if count == 0:
		print('Data kosong')
	else:
		rata2 = round(sum / count)
		print(count)
		print(countP)
		print(countT)
		print(rata2)



			