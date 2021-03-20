def sum_series(n):
    x=0
    add=0
    while n-x>0:
        add=(n-x)+add
        x=x+2
    return add
print(sum_series(10))
        
