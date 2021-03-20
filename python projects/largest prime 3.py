def find(n):
	prime=[1]*n
	prime[0]=0
	prime[1]=0
	index=3
	while index*index<=n:
		if prime[index]==1:
			for k in range(index*index,n,index):
				prime[k]=0
		index=index+2
	return prime

for i in range(int(input())):
    x,y=map(int,input().split())
    p=find(y+20)
    if 1 in p[x:y+1]:
        for j in range(y,x-1,-1):
                    if p[j]==1 and (j%2!=0 or j==2):
                        print(j)
                        break
        else:
                    print(-1)
    else:
        print(-1)
    
