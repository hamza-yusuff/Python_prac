from sys import stdin
for line in stdin:
    x,y=map(int,line.split())
    y=max([x,y])
    x=min([x,y])
    n=y-x+1
    result=n*x+((n*n)/2)-(n/2)
    print('Sum of {} to {} is -> {};'.format(x,y,int(result)))
