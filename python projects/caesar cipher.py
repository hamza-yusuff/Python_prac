
word=input()
w=list(word)
shift=int(input())
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
for i in range(len(word)):
    if w[i] in upper:
        index=upper.index(w[i])
        f=index+shift%26
        if f>=26:
            f=abs(26-(index+shift%26))
        
        w[i]=upper[f]
    elif w[i] in lower:
        index=lower.index(w[i])
        f=index+shift%26
        if f>=26:
            f=abs(26-(index+shift%26))
        
        w[i]=lower[f]
   
print(''.join(w))
