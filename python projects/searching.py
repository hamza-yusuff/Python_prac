def search(array,x,r,l):
    
    while r<=l:
        mid=int((l+r)/2)
        if array[mid]==x:
            return True
        elif array[mid]<x:
            r=mid+1
        elif array[mid]>x:
            l=mid-1
    return False

a,n=map(int,input().split())
array=list(map(int,input().split()))
for i in range(n):
	start,end,find=map(int,input().split())
	if search(array,find,start-1,end-1)==True:
		print("YES")
	else:
		print("NO")
