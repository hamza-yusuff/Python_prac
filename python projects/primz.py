n=7368790
prime=[1]*n
prime[0]=0
prime[1]=0
index=2
while index*index<=n:
    if prime[index]==1:
        for i in range(index*index,n,index):
            prime[i]=0
    index=index+1
num=int(input())
x=0
for k in range(n):
    if prime[k]==1:
        x=x+1
    if x==num and prime[k]==1:
        print(k)
        break




n=int(input())
upper=7368790
numbers=[1]*upper
numbers[0]=0
numbers[1]=0
i=2
while i*i<=upper:
    if numbers[i]==1:
        for k in range(i*i,upper,i):
            numbers[k]=0
    i=i+1
find=0
for g in range(upper):
    if numbers[g]==1:
        find=find+1
    if numbers[g]==1 and find==n:
        print(g)
        break
