#Nama / NIM : Faishal Zharfan / 16519278
#Problem : soal 2
#Tanggal : 26-03-2020

# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 
# KAMUS
# Variabel
#    N : int

def GambarBelahKetupat(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
# KAMUS LOKAL
# N : int

    array = [[' ' for j in range(N)] for i in range(N)]

    for i in range(int((N+1)/2)):
    	for j in range(int((N-(2*i+1))/2),int((N+(2*i+1))/2)):
    		array[i][j] = '*'

    for i in range(int((N+1)/2),N):
    	for j in range(int((2*i+2)/2)-int((N+1)/2),N-int((N+1)/2)+(N-i)):
    		array[i][j] = '*'

    for i in range(int((N+1)/2)-1):
    	for j in range(int((N+(2*i+1))/2),N):
    		array[i][j] = ''

    for i in range(int((N+1)/2),N):
    	for j in range(N-int((N+1)/2)+(N-i),N):
    		array[i][j] = ''

    for i in range(N):
    	for j in range(N):
    		print(array[i][j], end='')
    	print()
 

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
# KAMUS LOKAL
# N : int

    if N > 0 and N%2 == 1:
    	return True
    else :
    	return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N)):  # lengkapi dengan pemanggilan fungsi IsValid
    GambarBelahKetupat(N)    # lengkapi dengan pemanggilan prosedur GambarBelahKetupat
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")