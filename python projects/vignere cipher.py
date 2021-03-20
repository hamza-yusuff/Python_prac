def encrypt(key,s):
    string=list(s)
    k=0
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] in alpha:
            c=alpha.index(s[i])
            r=alpha.index(key[k])
            t=(c+r)%26
            string[i]=alpha[t]
            if k==len(key)-1:
                k=0
            else:
                k=k+1
        
    return ''.join(string)
print(encrypt("seven","khawarizmi"))
       
def decrypt(key,s):
    string=list(s)
    k=0
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] in alpha:
            c=alpha.index(s[i])
            r=alpha.index(key[k])
            t=(c-r+26)%26
            string[i]=alpha[t]
            if k==len(key)-1:
                k=0
            else:
                k=k+1
    return ''.join(string)

print(decrypt("seven",encrypt("seven","khawarizmi")))
