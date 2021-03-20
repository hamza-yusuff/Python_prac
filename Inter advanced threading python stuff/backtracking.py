def permutation(list,start,end):
    print("start : ",start, "end : ", end)
    
    if start==end:
        print(list)
    else:
        for i in range(start,end+1):
            list[start],list[i]= list[i],list[start]
            print("list: ", list)
            permutation(list,start+1,end)
            list[start],list[i]= list[i],list[start]

def normal(list,s):
    if s==1:
        print(list)
    else:
        for i in range(s):
            
            list[1]=list[s]
            normal(list,s-1)
            list[i]=list[s]

def combinations(k,n,list):
    if sum(l)==n:
        return list.append(l)
    else:
        for i in range(1,10):
            l.append(i)
            combinations(k,

        
        
