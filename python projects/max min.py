n=int(input())
k=int(input())
array=[]
low=10000000000000
for i in range(n):
    array.append(int(input()))
f=0
for j in range(k,n,k):
    new=array[f:j]
    if (max(new)-min(new)) <low:
        low=max(new)-min(new)
    f=j
print(low)


