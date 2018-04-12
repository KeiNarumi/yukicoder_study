N = int(input())
A = list(map(int,input().split()))
A.sort()
P = N//2
if(N%2==0):
    print((A[P-1]+A[P])/2)
else:
    print(A[P])