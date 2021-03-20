n=int(input())
string=input()
k=0
valley=0
while k<len(string):
    if string[k]=="U":
        m=[]
        j=k
        while j<len(string):
            if string[j]=="U":
                m.append("U")
            else:
                m.pop()
            j=j+1
            if len(m)==0:
                break
        k=j
        
    elif string[k]=="D":
        v=[]
        g=k
        while g<len(string) :
            if string[g]=="D":
                v.append("D")
            else:
                v.pop()
            g=g+1
            if len(v)==0:
                break
        k=g
        if len(v)==0:
            valley=valley+1
print(valley)
        
    
