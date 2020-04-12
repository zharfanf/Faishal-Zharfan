abis = False
panjang = len(nums)
n = 0
while n < panjang and not(abis):
    for i in range(panjang):
        if nums[i] == val:
            nums.pop(i)
            panjang = panjang - 1
            break
        elif nums[-1] != val:
            abis = True
print(nums)