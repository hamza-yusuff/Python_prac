n=int(input())
num=[i for i in range(n)]
index=2
while index<=n:
    if n%index==0:
        for k in range(index,n,index):
            num[k]=0
    index=index+1

c=0
for j in range(1,n):
    if num[j]!=0:
        c=c+1
print(c)
