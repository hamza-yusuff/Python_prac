while True:
    x,y=map(int,input().split())
    res=list(str(pow(x,2)))
    for i in range(len(res)//2+1):
       res[i]=int(res[i])+1
    final=res[:int(len(res)/2)+1]+res[int(len(res)/2)-1::-1]
    print(''.join(list(map(str,final))))

    
