L=int(input())
N=int(input())
W=sorted(map(int,input().split()))
num=0

for i in range(N):
    if(L-W[i]<0):
        break
    else:
        L-=W[i]
        num+=1
print(num)