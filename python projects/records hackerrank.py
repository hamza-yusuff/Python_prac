num=int(input())
array=list(map(int,input().split()))
lowchange=0
highchange=0
hell=array[:1]
high=max(hell)
low=min(hell)

for i in range(2,len(array)+1):
   hell=array[:i]
   if max(hell)>high:

    highchange=highchange+1
    high=max(hell)
   if min(hell)<low:
    lowchange=lowchange+1
    low=min(hell)
print(highchange,lowchange)

    


