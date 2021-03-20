string=input()
uppercase=0
lowercase=0
for i in range(len(string)):
	store=str(string[i])
	if store.isupper()==True:
		uppercase=uppercase+1
	elif store.islower()==True:
		lowercase=lowercase+1
print(uppercase, lowercase)
