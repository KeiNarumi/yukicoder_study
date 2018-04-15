A = [int(input()) for i in range(2)]
i = A[1]
while(True):
    if (i == 1):
        break
    A[0] = A[0]-(A[0]//(i**2))
    i-=1
print(A[0])