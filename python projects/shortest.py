import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
def find(r):
    dev=divisorGenerator(res)
    for x in range(len(dev)):
        if dev[x]>m or dev[x]>n:
            dev.remove(dev[x])
    return dev
def search(i):
    if divisor[i]<m and divisor[i+1]<n:
        r=divisor[i]
        c=divisor[i+1]
    else:
        r=divisor[i+1]
        c=divisor[i]
    move=array[r][c]
    return move

m=int(input())
n=int(input())
array=[]
for i in range(m):
   hello=list(map(int,input().split()))
   array.append(hello)
found=True
memo={}
while found==True:
    res=array[0][0]
    divisor=find(res)
    possible=[]
    for k in range(0,len(divisor),2):
        possible.append(search(k))
    
    
    
