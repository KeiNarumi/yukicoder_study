def J_triple(i):
    if(i%3==0):
        return True
    else:
        return False

def J_any3(i):
    while(i>0):
        if(i%10==3):
            return True
        i=i//10
    return False

A,B = map(int,input().split())
for i in range(A,B+1):
    if(J_triple(i) or J_any3(i)):
        print(i)
