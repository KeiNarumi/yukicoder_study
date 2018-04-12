N,K=map(int,input().split())

if(N==K):
    print("draw")
elif((N==0 and K==1)or(N==1 and K==2)or(N==2 and K==0)):
    print("Won")
else:
    print("Lost")