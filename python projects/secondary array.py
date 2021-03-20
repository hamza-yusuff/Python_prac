secondary=[[r for r in range(2)]for c in range(2)]
for r in range(2):
    for c in range(2):
        secondary[r][c]=input('enter')
def output(secondary):
    for r in range(2):
        for c in range(2):
           print(secondary[r][c],end=' ')
        print('\n')
output(secondary)       
def verticaloutput(array):
    for r in range(2):
        for c in range(1,-1,-1):
            print(secondary[r][c],end=' ')
        print('\n')
verticaloutput(secondary)
    
def actualvertical(secondary):
    for r in range(2):
        temp=secondary[r][1]
        secondary[r][1]=secondary[r][0]
        secondary[r][0]=temp
    return secondary
output(actualvertical(secondary))

