f,s=map(int,input().split())
one=list(map(int,input().split()))
second=list(map(int,input().split()))
num=0


for i in range(1,max(second)+1):
    f=True
    for k in range(len(second)):
        if second[k]%i!=0:
            f=False
            break
    if f==True:
        for j in range(len(one)):
            if i%one[j]!=0:
                f=False
                break
    if f==True:
        num=num+1
print(num)
    
        
