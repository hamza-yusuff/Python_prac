array="1abcdefghjiklmnopqrstuvwxyz"
word=input()
w=list(word)
for i in range(len(word)):
    if w[i] in array:
        pos=array.index(w[i])
        new=(pos**7)
        x=new%15
        w[i]=array[x]
print(''.join(w))
    
