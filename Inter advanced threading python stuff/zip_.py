x=[1,2,3,4]
y=[1,2,3,7,9]

print(list(zip(x,y)))

for i,j in zip(x,y):
    if i==j:
        print("same", i)
    else:
        print("not same", i,j)

##enumerate
l=[]
for z,element in enumerate(y):
  l.append([z,element])

print(dict(l))

