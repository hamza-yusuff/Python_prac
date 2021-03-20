for i in range(int(input())):
    n=int(input())
    high=-1
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            high=k
    if high==-1:
        print(n-1)
    else:
        print(int(max([n/high,high])-min([n/high,high])))
