num,x,y=map(int,input().split())
if x==y:
    print(int(num/2),int(num/2))
else:
    for k in range(1,num):
      if (k/(num-k))==(x/y) or (num-k)/k==(y/x):
          print(k, num-k)
          break

