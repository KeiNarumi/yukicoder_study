coins = []
osatu = 0
for i in range(3):
    coins.append(int(input()))
while(True):
    if(coins[2]<25):
        break
    else:
        coins[2]-=25
        coins[1]+=1
while(True):
    if(coins[1]<4):
        break
    else:
        coins[1]-=4
        coins[0]+=1
while(True):
    if(coins[0]<10):
        break
    else:
        coins[0]-=10
        osatu+=1
print(coins[0]+coins[1]+coins[2])
