n=int(input())
upper=7368790
numbers=[1]*upper
numbers[0]=0
numbers[1]=0
i=3
while i*i<=upper:
    if numbers[i]==1:
        for k in range(i*i,upper,i):
            numbers[k]=0
    i=i+2
find=0
for g in range(upper):
    if numbers[g]==1 and g%2!=0:
        find=find+1
    if numbers[g]==1 and find==n and g%2!=0:
        print(g)
        break
    


