def change(word):
    word=list(word)
    for i in range(len(word)):
        if word[i]=='b':
            word[i]='6'
        elif word[i]=='6':
            word[i]='b'
        elif word[i]=='9':
            word[i]='g'
        elif word[i]=='g':
            word[i]='9'
        elif word[i]=='1':
            word[i]='l'
        elif word[i]=='l':
            word[i]='1'
        elif word[i]=='0':
            word[i]='o'
        elif word[i]=='o':
            word[i]='0'
        elif word[i]=='5':
            word[i]='s'
        elif word[i]=='s':
            word[i]='5'
        elif word[i]=='z':
            word[i]='2'
        elif word[i]=='2':
            word[i]='z'
    res=''.join(word)
    return res
string=input()
while string!='the end.':
    string=string.split(' ')
    new=[]
    for k in range(len(string)):
        new.append(change(string[k]))
    print(' '.join(new))
    string=input()
