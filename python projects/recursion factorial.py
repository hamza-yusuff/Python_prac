def traversal(num):
    if num==1:
        return 1
    else:
        return num*traversal(num-1)
print(traversal(100))
while True:
    print('SANI IS HOT')
