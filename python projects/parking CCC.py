number=int(input())
row1=list(input())

row2=list(input())
c=0
for i in range(number):
    if row1[i]==row2[i]=='C':
        c=c+1
print(c)
