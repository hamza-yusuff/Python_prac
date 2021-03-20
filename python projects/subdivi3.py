s=input()
c=0
for i in range(len(s)):
    for k in range(1,len(s)+1):
        new=s[i:k]
        n=list(map(int,list(new)))
        print(sum(n))
        if sum(n)%3==0 and sum(n)!=0:
            c=c+1
print(c)
        
