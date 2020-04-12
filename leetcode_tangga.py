
if n == 1:
    return 1
elif n ==2 :
    return 2
elif n == 3:
    return 3
else:
    count = 3
    hitung = 0
    for i in range(n-3):
        for j in range(2+hitung):
            count = count + 1
            hitung = hitung + j
    return count