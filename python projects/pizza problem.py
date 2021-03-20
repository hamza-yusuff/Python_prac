t,x,y,z,m=map(int,input().split())
if t-m<=0:
    print('NO')
else:
    res=(1/(x*60))+(1/(y*60))+(1/(z*60))
    new=(1/res)/60
    if new<=t-m:
        print('YES')
    else:
        print('NO')
