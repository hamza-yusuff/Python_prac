string='IJ TPGEPS BMJ'
string=list(string)
for i in range(len(string)):
	if string[i]!=' ' and ord(string[i])==65:
		string[i]=90
	if string[i]!=' ':
		string[i]=chr(ord(string[i])-1)

print(''.join(string))
