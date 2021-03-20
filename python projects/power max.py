q=int(input())
for c in range(q):
	x,y=input().split()
	x=int(x)
	y=int(y)
	if x==2:
		t=c+1
		sent='Case #'+str(t)+str(y)
		print(sent)
	else:
	    new=[]
	    i=1
	    res=(x**y)**i
	    while res>2:
		    i=i+1
		    res=(x**y)**(1/i)
		    if res-int(res)==0:
			    new.append(i)
	    t=c+1
	    sentence='Case #'+str(t)+':'+str(max(new))
	    print(sentence)
			
