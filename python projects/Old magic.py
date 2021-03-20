number=int(input())
operation=[]
operand=[]
for i in range(number):
	x,y=input().split()
	operation.append(x)
	operand.append(y)
res=int(input())
for k in range(number-1,-1,-1):
	if operation[k]=='multiply':
		res=res//int(operand[k])
	elif operation[k]=='divide':
		res=res*int(operand[k])
	elif operation[k]=='add':
		res=res-int(operand[k])
	elif operation[k]=='subtract':
		res=res+int(operand[k])
print(res)
