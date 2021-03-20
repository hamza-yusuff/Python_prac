for t in range(int(input())):
	n=int(input())
	num=[1]*510
	num[0]=0
	num[1]=0
	index=2
	while index*index<=n:
		if num[index]==1:
			for i in range(index*index,510,index):
				num[i]=0
		index=index+1
	small=[]
	find=False
	for j in range(n-20,510):
		if j==n:
			find=True
		if num[j]==1 and find==False:
			small.append(j)
		if find==True and num[j]==1 and j!=n:
			small.append(j)
			break
	print(small[-2],small[-1])
