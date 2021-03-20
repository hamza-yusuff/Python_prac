i=list(map(int,input().split()))
h=sorted(i)
j=[h[-1],h[-2],h[-3],h[-4]]
k=[h[0],h[2],h[1],h[3]]
print(sum(j),sum(k))
