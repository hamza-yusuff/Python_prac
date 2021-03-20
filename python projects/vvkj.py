num=int(input())
for i in range(num):
	x,y,z=input().split()
	value=[]
	if int(x)+int(y)>=int(z):value.append(True)
	if int(y)+int(z)>=int(x):value.append(True)
	if int(z)+int(x)>=int(y):value.append(True)
	if value.count(True)==3:
		print('Yes')
	else:
		print('No')
