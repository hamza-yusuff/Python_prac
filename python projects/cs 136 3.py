c=input()
at_the_rate=0
space=0
while (c!='end'):
    if c=='@':
        if space==0:
            at_the_rate+=1
        else:
            print('-',space, end=' ')
            space=0
            at_the_rate=1
    elif c==' ':
        if at_the_rate==0:
            space+=1
        else:
            print(at_the_rate,end=' ')
            at_the_rate=0
            space=1
    else:
        if at_the_rate!=0:
            print(at_the_rate, end=' ')
        else:
            print('-',space, end=' ')
        print(0,end='\n')
        at_the_rate=0
        space=0
    c=input()
