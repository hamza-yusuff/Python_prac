
for i in range(int(input())):
    x,y=map(int,input().split())
    s=0
    for k in range(1,x+1):
        s=s+pow(k,y)
    print(pow(s,1,1000000007))
