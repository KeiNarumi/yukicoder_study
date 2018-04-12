str = list(input())
strA = []
for i in range(0,len(str)):
	try:
		strA.append(int(str[i]))
	except ValueError:
		pass
print(sum(strA))