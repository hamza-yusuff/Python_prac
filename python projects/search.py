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
def searching(array,x,r,l):
    if r<=l:
        mid=int((l+r)/2)
        if array[mid]==x:
            return True
        elif array[mid]<x:
            return searching(array,x,mid,l)
        else:
            return searching(array,x,r,mid)
    else:
        return False

a=list(map(int,input().split()))
n=int(input())
print(searching(a,n,0,len(a)-1))

