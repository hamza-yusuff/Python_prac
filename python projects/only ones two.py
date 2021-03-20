while True:
    l=len(input())//2
    print(*range(2,l+2),*range(l,1,-1),sep='')
