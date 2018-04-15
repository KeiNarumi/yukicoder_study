def FizzBuzzString(N):
    strs = [("Fizz"*(i%3==0) + "Buzz"*(i%5==0)) or i for i in range(1,N+1)]
    m_str = ''.join(map(str,strs))
    return m_str

N = int(input())
i = 0
for j in FizzBuzzString(N):
    if(j=="z"):
        i+=1
print(i)