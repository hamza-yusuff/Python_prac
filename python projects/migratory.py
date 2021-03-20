n=int(input())
array=list(map(int,input().split()))
highest=[]
a=list(set(array))

high=-1
for i in range(len(a)):
    if array.count(a[i])>high:
        high=array.count(a[i])
        highest.append(a[i])
highest.sort()
print(highest)
if len(highest)>1:
    print(highest[1])
else:
    print(highest[0])
