prime=[1]*10010
prime[0]=0
prime[1]=0
index=3
while index*index<=10010:
    if prime[index]==1:
        for k in range(index*index,10010,index):
            prime[k]=0
    index=index+2

for i in range(int(input())):
    x,y=map(int,input().split())
    if 1 in prime[x:y+1]:
        for j in range(y,x-1,-1):
                    if prime[j]==1 and (j%2!=0 or j==2):
                        print(j)
                        break
        else:
                    print(-1)
    else:
        print(-1)
    
