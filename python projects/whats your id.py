dept={115:'CSE',141:'EEE',116:'BBA',117:'LLB',114:'English',111:'Economics'}
term=[0,'Spring','Summer','Autumn']
test=int(input())
for i in range(test):
	hell=[]
	card=list(input().split('-'))
	for x in dept:
		if x==int(card[1]):
			hell.append(dept[x])
	t=str(card[0])
	hell.append(term[int(t[-1])])
	hell.append('20'+t[:2])
	print(' '.join(hell))
