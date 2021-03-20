for i in range(int(input())):
    string=list(map(str,input().split()))
    for k in range(len(string)):
        f=string[k]
        new=[]
        for j in range(len(string[k])):
            if j!=len(f)-1:
                if f[j]!=f[j+1]:
                    new.append(f[j])
            else:
                new.append(f[j])
        string[k]=''.join(new)
        
    print(' '.join(string))
