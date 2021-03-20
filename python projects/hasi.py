t,x=map(int,input().split())
l=1
c=0
while l<t:
        
        mid=int((l+t)/2)
        c=c+1
        if mid<x:
            t=mid
        else:
            l=mid+1


print(c)
