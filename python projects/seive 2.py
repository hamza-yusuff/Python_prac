import math
def seive(n):
	primes=[True for i in range(3,n+1,2)]
	
	f=[]
	for k in range(3,int(math.sqrt(n))+1):
		if primes[k]==True:
			f.append(k)
			for j in range(k*k,n+1,k):
				if primes[j]==True:
					primes[j]=False
	return f
print(seive(100))
