x,y=input().split()
numbers1=input().split(' ')
numbers2=input().split(' ')
numbers1=set(numbers1)
numbers2=set(numbers2)
if len(numbers1)==int(x) and len(numbers2)==int(y):
    together=numbers1|numbers2
    together=sorted(list(together))
    print(' '.join(together))
