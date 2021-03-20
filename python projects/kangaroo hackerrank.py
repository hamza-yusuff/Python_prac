x1,v1,x2,v2=map(int,input().split())
time=(x2-x1)/(v1-v2)
print(time)
if time!=int(time) and time<0:
    print("NO")
else:
    print("YES")
