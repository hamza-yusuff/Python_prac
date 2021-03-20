for i in range(1,int(input())+1):
	score=[]
	handle=[]
	for k in range(int(input())):
		name,rating=input().split()
		handle.append(name)
		handle.append(rating)
		score.append(rating)
	score=list(map(int,score))
	highest=max(score)
	new=[]
	while str(highest) in handle:
		m=handle[handle.index(str(highest))-1]
		new.append(m)
		handle.remove(str(highest))
	new.sort()
	if highest>=1600 and highest<=1899:
		print("Case {}: {} is Expert!.".format(i,new[0]))
	elif highest>=1400 and highest<=1599:
		print("Case {}: {} is Specialist!.".format(i,new[0]))
	elif highest>=1200 and highest<=1399:
		print("Case {}: {} is Pupil!.".format(i,new[0]))
	else:
		print("Case {}: {} is Newbie!.".format(i,new[0]))
	
		
