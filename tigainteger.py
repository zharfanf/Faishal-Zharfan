#Nama / NIM : Faishal Zharfan / 16519278
#Problem : soal 1
#Tanggal : 26-03-2020

# Program TigaInteger
# Input: 3 integer: A, B, C
# Output: Sifat integer dari A, B, C (positif/negatif/nol dan ganjil/genap) 
#         Nilai maksimum, minimum, dan nilai tengah
 
# KAMUS
# variabel
#    A, B, C : int
#    nilaitengah : int
 
# PROCEDURE DAN FUNCTION
def CekInteger (x):
# I.S.: x terdefinisi, bertype int
# F.S.: Jika x positif dan genap, maka tertulis di layar: POSITIF-GENAP
#       Jika x positif dan ganjil, maka tertulis di layar: POSITIF-GANJIL
#       Jika x negatif, maka tertulis di layar: NEGATIF
#       Jika x nol, maka tertulis di layar: NOL
# Tuliskan realisasi prosedur CekInteger di bawah ini
#REALISASI
	if x > 0 :
		if x%2 == 0:
			print("POSITIF-GENAP")
		else:
			print("POSITIF-GANJIL")
	elif x < 0:
		print("NEGATIF")
	else:
		print("NOL")
              
def Max (a, b, c):
# menghasilkan nilai terbesar di antara a, b, c (integer)
# Tuliskan realisasi fungsi Max di bawah ini
	if a > b :
		if b > c:
			return a
		elif c > a :
			return c
		else :
			return a	
	elif b > c :
		if c > a:
			return b
		elif a > b :
			return a
		else:
			return b
	elif c > a :
		if a > b:
			return c
		elif b > c:
			return b
		else:
			return c
	elif a == b and b == c:
		return a
     
def Min (a, b, c):
# menghasilkan nilai terkecil di antara a, b, c (integer)
# Tuliskan realisasi fungsi Min di bawah ini
	if a < b :
		if b < c:
			return a
		elif c < a :
			return c
		else:
			return a
	elif b < c :
		if c < a:
			return b
		elif a < b :
			return a
		else:
			return b
	elif c < a :
		if a < b:
			return c
		elif b < c :
			return b
		else:
			return c
	elif a == b and b == c:
		return a
            
# PROGRAM UTAMA
# Input
A = int(input())
B = int(input())
C = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)

# Penulisan maksimum, minimum, dan nilai tengah
print(Max(A,B,C))
print(Min(A,B,C))
nilaitengah = A + B + C - Max(A,B,C) - Min(A,B,C) 
print(nilaitengah)