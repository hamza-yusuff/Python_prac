num=int(input())
carry=input()
new=carry.split(' ')
res=[]
t=1
total=0
for i in range(num):
	total=total+int(new[i])
	res.append(total/t)
	t=t+1
for l in range(num):
	print('{:.10f}'.format(res[l]))
