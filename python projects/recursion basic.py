def output(num):
    if num==0:
        return None
    else:
        print(2)
        output(num-1)
print(output(5))
