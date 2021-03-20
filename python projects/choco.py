n=int(input())
array=list(map(int,input().split()))
d,m=map(int,input().split())
if len(array)==m:
    if sum(array)==d:
        print(1)
    else:
        print(0)
else:
    count=0
    for i in range(len(array)-m):
        print(array[i:i+m])
        if sum(array[i:i+m])==d:
            count=count+1
    print(count)
