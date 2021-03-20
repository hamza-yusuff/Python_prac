import math
for i in range(int(input())):
	x,y=map(int,input().split())
	for k in range(1,y):
		if (x*k)%y==1:
			print("Yes")
			break
	else:
		print("No")
	
