def divisible(n):
    if len(str(n))==2:
        if n%7==0:
            return True
        else:
            return False
    else:
        f=str(n)
        num=int(f[-1])*2
        res=int(f[:-1])-num
        return divisible(res)
print(divisible(int(input())))
