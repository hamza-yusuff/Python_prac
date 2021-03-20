import math
def isperfect(num):
    sqrt=int(num**0.5)
    if sqrt**2==num:
        return True
    else:
        return False




for i in range(int(input())):
	num=int(input())
	perf1=5*((num)**2)+4
	perf2=5*((num)**2)-4
	
	if isperfect(perf1)==True or isperfect(perf2)==True: 
		print("YES")
	else:
		print("NO")
