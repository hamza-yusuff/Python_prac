test=int(input())
for i in range(test):
	num=int(input())
	string=input()
	d=list(set(string))
	bang=True
	for k in range(len(d)):
		freq=string.count(d[k])
		if freq>num/2:
			print(1)
			bang=False
			break
	if bang==True:
		print(0)

