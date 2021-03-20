test=int(input())
for i in range(1,test+1):
    num=input()
    res=int(int(num)/10)
    if int(num)==1900:
        print('Case #{}: 19th century!'.format(i))
    
    elif len(str(res))==2:
        if int(num)%10==0 and num[1:]=='00':
            print('Case #{}: {}th century!'.format(i,num[0]))
        else:
            print('Case #{}: {}th century!'.format(i,int(num[0])+1))
    else:
        if int(num)%10==0 and num[2:]=='00':
            if int(num[1:2])==0 or int(num[1:2])>=4:
                print('Case #{}: {}th century!'.format(i,num[:2]))
            elif int(num[1:2])==2:
                print('Case #{}: {}nd century!'.format(i,num[:2]))
            elif int(num[1:2])==3:
                print('Case #{}:{}rd century!'.format(i,num[:2]))
            elif int(num[1:2])==1:
                print('Case #{}: {}st century!'.format(i,num[:2]))

        else:
            if int(num[:2])>=10 and int(num[:2])<=19:
                print('Case #{}: {}th century!'.format(i,int(num[:2])+1))
            else:
                if int(num[1:2])==0:
                    print('Case #{}: {}st century!'.format(i,int(num[:2])+1))
                elif int(num[1:2])==1:
                    print('Case #{}: {}nd century!'.format(i,int(num[:2])+1))
                elif int(num[1:2])==2:
                    print('Case #{}: {}rd century!'.format(i,int(num[:2])+1))
                else:
                    print('Case #{}: {}th century!'.format(i,int(num[:2])+1))
