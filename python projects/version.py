x,y=input().split()
first=x.split('.')
second=y.split('.')
if int(first[0])>int(second[0]):
	print(x)
elif int(first[0])==int(second[0]):
	if int(first[1])==int(second[1]):
		if int(first[2])>int(second[2]):
			print(x)
		else:
			print(y)
	elif int(first[1])>int(second[1]):
		print(x)
	else:
		print(y)
else:
	print(y)
