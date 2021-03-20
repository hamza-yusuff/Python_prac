def primebetter2(n):
    if n%2==0:
        return False
    else:
        maximum=n**0.5+1
        for x in range(3,int(maximum),2):
            if n%x==0:
                return False
                break
        else:
            return True
def divisor(n):
	dev=[]
	for k  in range(1,n+1):
		if n%k==0:
			dev.append(k)
	return dev
test=int(input())
for c in range(test):
	num=int(input())
	if primebetter2(sum(divisor(num)))==True:
		print('Yes')
	else:
		print('No')
