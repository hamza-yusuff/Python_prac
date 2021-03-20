memo={}
def fibonacci(n):
    if n in memo:
        return memo[n]
    elif n==1 or n==2:
        memo[n]=1
        return 1
    else:
        f=fibonacci(n-1)+fibonacci(n-2)
        memo[n]=f
        print(memo[n])
        return memo[n]
print(fibonacci(6))
#1,1,2,3,5,8,13
