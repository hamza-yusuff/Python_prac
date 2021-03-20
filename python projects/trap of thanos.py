test=int(input())
for i in range(1,test+1):
	ax,ay,bx,by,cx,cy=map(int,input().split())
	l=input()
	if l=='A':
		middlex=(bx+cx)/2
		middley=(by+cy)/2
		res=((ax-middlex)**2+(ay-middley)**2)**0.5
	elif l=='B':
		middlex=(ax+cx)/2
		middley=(ay+cy)/2
		res=((bx-middlex)**2+(by-middley)**2)**0.5
	elif l=='C':
		middlex=(bx+ax)/2
		middley=(by+ay)/2
		res=((cx-middlex)**2+(cy-middley)**2)**0.5
	print('Case {}: {:.3f}'.format(i,res))
