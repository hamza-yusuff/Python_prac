num=int(input())
if num==1:
	print(2)
elif num==2:
	print(3)
elif num==3:
	print(5)
else:
	prime=6*(num-3)+1
	prime2=6*(num-3)-1
	if prime2%2!=0 and prime2%3!=0 and prime2%5!=0 and prime%2!=0 and prime%3!=0 and prime%5!=0:
		print(prime2)
	elif (prime2%2!=0 and prime2%3!=0 and prime2%5!=0) and (prime%2==0 or prime%3==0 or prime%5==0):
		print(prime2)
	else:
		print(prime)
