def sumdigit(num):
    num=str(num)
    if len(num)==1:
        return num
    else:
        return int(num[0])+int(sumdigit(num[1:]))
print(sumdigit(1001))
