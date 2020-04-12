import csv

def login(username, password):
	bener = False
	with open("User.csv", 'r') as csvfile:
		fooreader = csv.reader(csvfile)
		foo = [r for r in fooreader]
		while not(bener):
			for i in range(len(foo)):
				if foo[i][3] == username and foo[i][4] == password:
					bener = True
					break
			if bener == False:
				print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi! ")
				username = input('Masukan username : ')
				password = input('Masukan password : ')

	return ("Selamat bersenang-senang, " + str(foo[i][0]) + "!" )

nama = input('Masukan username : ')
passw = input('Masukan password : ')
print(login(nama, passw))