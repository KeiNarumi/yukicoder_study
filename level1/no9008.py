NumOfNumber = int(input())
N=input()
Numbers=N.split()
sum=0
for i in range(NumOfNumber):
    sum+=int(Numbers[i])
print(sum)
