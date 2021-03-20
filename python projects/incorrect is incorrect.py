string=input()
plus=string.index("+")
equal=string.index("=")
a=int(string[:plus])
c=int(string[plus+1:equal])
d=int(string[equal+1:])
if (a+c+d)%2!=0:
	print("Impossible")
else:
	f=(a+c+d)//2
	s=f//2
	print(str(s)+str(s)+'='+str(f))
