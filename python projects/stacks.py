for i in range(int(input())):
    string=input()
    first='([{'
    second=')]}'
    cha=[]
    for i in range(len(string)):
        if string[i] in first:
            cha.append(string[i])
        if string[i] in second:
            if not cha:
                print("NO")
                break
            p=first.index(cha[-1])
            if second[p]==string[i]:
                cha.pop()
            else:
                print("NO")
                break
    else:
        print("YES")
                
                
        
