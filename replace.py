import csv
import shutil
from tempfile import NamedTemporaryFile
user = input("Masukan Username : ")

username = ""
saldo = "1000"

with open("User.csv", 'r') as file:
	valid  = csv.reader(file)
	array = [i for i in valid]
	for i in range(len(array)):
		if array[i][0] == user:
			username = username +  str(array[i][0])
			saldo = str(int(saldo) + int(array[i][6]))
			break
if username != "" and saldo != "":
	with open("coba_replace.csv", 'a') as csvfile:
		write = csv.writer(csvfile, delimiter=',')
		write.writerow([username, saldo])
else:
	print("Tidak ada")


#out =  open("coba_replace.csv", 'r')
#data = csv.reader(out)
#data = [[row[0],eval(row[1])] for row in data]
#out.close()
#for i in range(len(itu)):
#	if itu[i][0] == user:
#		saldo = itu[i][1]
#print(data)
#print(type(data[1][1]))
#with open("coba_replace.csv", 'w') as csvfile:
#	eta = csv.reader(csvfile)
#	oto = [j for j in eta]
#	for j in range(len(oto)):
#		if oto[j][0] == user:
#			oto[j][1] = oto[j][1] + 2000

# filename = "coba_replace.csv"
# temp_file = NamedTemporaryFile(delete=False)

# with open(filename,'r+', encoding='utf-8') as csvfile, temp_file:
# 	reader = csv.DictReader(csvfile)
# 	fieldnames = ['username', 'saldo']
# 	writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
# 	#writer.writerheader()
# 	for row in reader:
# 		if row['username'] == user:
# 			row['saldo'] = int(row['saldo']) + 100
# 			print(row)
# 		writer.writerow(object(row))


	# shutil.move(temp_file.name, filename)
