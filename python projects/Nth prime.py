import math
def seive(n):
	primes=[True for i in range(n+1)]
	primes[0]=False
	primes[1]=False
	f=[]
	for k in range(2,int(math.sqrt(n))+1):
		if primes[k]==True:
			f.append(k)
		for j in range(k*k,n+1,k):
			if primes[j]==True:
				primes[j]=False
	return f
n=int(input())
p=seive(7368790)
print(p[n-1])


