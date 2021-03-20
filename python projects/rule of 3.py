ruleb=['AA','AB','B']
rulea=['AB','BB','AA']
string='AB'
c=0
while string!='AAAB':
    c=c+1
    print(string)
    if ruleb[0] in string:
        string=string.replace(ruleb[0],rulea[0])
    elif ruleb[1] in string:
        string=string.replace(ruleb[1],rulea[1])
    else:
        string=string.replace(ruleb[2],rulea[2])
        
print(c)      
