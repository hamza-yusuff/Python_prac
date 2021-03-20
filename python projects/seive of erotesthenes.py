import math
import time
def prime(n):
    primes=[True for i in range(n+1)]
    primes[0]=False
    primes[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        for  k in range(i*i,n+1,i):
            if primes[k]==True:
                primes[k]=False
    return primes
p=prime(500000)

