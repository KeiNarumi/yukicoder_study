N = int(input())
box = []
if(N>0):
    while(N>1):
        box.append(1)
        N-=2
    if(N==1):
        box[0]=7
else:
    box.append(0)
m_box = map(str,box)
print(''.join(m_box))