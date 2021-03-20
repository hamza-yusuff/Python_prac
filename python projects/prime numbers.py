def primebasic(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True

def primebetter(n):
    maximum=n**0.5+1
    for t in range(2,int(maximum)):
        if n%t==0:
            return False
            break
    else:
        return True
def primebetter2(n):
    if n==2:return True
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
print(primebetter2(3))
