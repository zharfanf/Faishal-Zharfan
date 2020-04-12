import csv
from datetime import datetime


def refund(Username, ID, Jumlah):
	date = datetime.now()
	valid  = False
	with open('tiket.csv', 'r') as csvfile:
		kepemilikan = csv.reader(csvfile)
		milik = [i for i in kepemilikan]
		for i in range(len(milik)):
			if milik[i][0] == Username:
				if milik[i][1] == ID and milik[i][2] == Jumlah:
					print("Uang refund sudah kami berikan pada akun Anda.")
					valid = True
					break
				else:
					print("Anda tidak memiliki tiket terkait.")
					break
	if valid == True:
		with open('refund.csv','a') as pencatatan:
			catat = csv.writer(pencatatan, delimiter=',')
			catat.writerow([Username,date.strftime("%d/%m/%y"),ID,Jumlah])
			# koleksi = [i for i in catat]

n = input("Masukan Username : ")
m = input("Masukan id wahana : ")
x = input("Masukan jumlah tiket : ")

refund(n,m,x)
		# with open('wahana.csv','r') as saldobalik:
		# 	daftar = csv.reader(saldobalik):
		# 	harga = [i for i in daftar]
		# 	for i in range(len(harga)):
		# 		if harga[i][0] == ID:
		# 			plus = harga[i][2] * 0.8
		# with open('')


