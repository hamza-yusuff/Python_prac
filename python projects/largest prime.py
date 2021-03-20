for i in range(int(input())):
	x,y=map(int,input().split())
	prime=[1]*10010
	prime[0]=0
	prime[1]=0
	index=2
	while index*index<=y:
		if prime[index]==1:
			for k in range(index*index,10010,index):
				prime[k]=0
		index=index+1
	p=[]
	for j in range(x,y+1):
		if prime[j]==1:
			p.append(j)
	if len(p)==0:
		print(-1)
	else:
		print(max(p))
		
	
