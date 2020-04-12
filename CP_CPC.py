input_1 = list(map(int,input("").split()[:3]))
i = 0
orang = [[] for i in range(input_1[1]-1)]

while i < input_1[1]-1:
	for j in range(input_1[0]**(i+1)):
		if i > 1:
			orang[i].append((input_1[0]**(i+1)) + (-1 + j))
		else:
			orang[i].append((input_1[0] * i) +  (1+j))
	i = i + 1

print(orang)


input_2 = list(map(int,input("").split()[:3]))
print(input_2[0])

while not(input_2[0] < input_2[1]) and not(input_2[1] < input_2[2]):
	input_2.sort()
for m in range(input_1[1]-1):
	del orang[m][int(((input_2[0] - 1 )/input_1[0])*len(orang[m])):int((input_2[0]/input_1[0])*(len(orang[m])))]

print(orang)

