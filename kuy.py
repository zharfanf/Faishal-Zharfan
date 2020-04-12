#NIM : 16519278
#Nama : Faishal Zharfan
#Program : Soal 6 / Responsi
#Tanggal : 08-04-2020

N = int(input(''))
i = 0
found = False
while (N <= 0 or N > 100):
    print("Masukan salah. Ulangi!")
    N = int(input(''))
AI = [int(input('')) for i in range(N)]
X = int(input(''))
if (X == 0):
    while not(found) and i < N:
        if AI[i] == 0:
            found = True
            hasil = AI[i]
        i = i + 1
    if found == True :
        print(i)
    else:
        print("Tidak ada 0")
elif ((X == -1)):
    while not(found) and i < N:
        if AI[i] < 0 :
            found = True
            hasil = AI[i]
        i = i + 1   
    if found == True :
        print(i, hasil)
    else:
        print("Tidak ada negatif")
elif ((X == 1)):
    while not(found) and i < N:
        if AI[i] > 0 :
            found = True
            hasil = AI[i]
        i = i + 1
    if found == True :
        print(i, hasil)
    else:
        print("Tidak ada positif")    
else:
    print("Tidak diproses")