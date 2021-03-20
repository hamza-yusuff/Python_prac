def gcd(a,c):
    if a==0:
        return c
    elif c==0:
        return a
    else:
        r=(a%c)
        return gcd(c,r)
l=int(input())
k=int(input())
print(gcd(l,k))
