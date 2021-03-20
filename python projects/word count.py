new=''
while True:
	try:
		var=input()
		new=new+' '+var
	except:
		break
array=new.split(' ')
number=list(map(lambda x:array.count(x),replica))
print(replica[number.index(max(number))])
