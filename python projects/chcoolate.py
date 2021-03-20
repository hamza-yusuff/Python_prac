n=int(input())
array=list(map(int,input().split()))
d,m=map(int,input().split())
c=0
for i in range(len(array)-m):
    if sum(array[i:i+m])==d:
        c=c+1
print(c)
