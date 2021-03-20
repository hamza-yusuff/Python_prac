num=int(input())
for i in range(1,num+1):
	word=input()
	if word==word[::-1]:
		print('Case {}: {}'.format(i,0))
	else:
		res=0
		for i in range(1,len(word)):
			new=list[word]
			extra=word[:-i]
			del new[i]
			if new==new[::-1]:
				res=res+1
				break
			elif extra==extra[::-1]:
				res=i
		                break
		
       print('Case {}: {}'.format(i,res))
			
			
