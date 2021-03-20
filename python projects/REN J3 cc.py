number=int(input())
new=['']
for i in range(number):
    string=list(input())
    k=0
    array=['']
    j=0
    while k<=len(string)-1:
        count=0
        while j>=k and j<len(string):
            if string[k]==string[j]:
                count=count+1
            else:
                break
            j=j+1
        sent=str(count)+' '+string[j-1]
        array.append(sent)
        k=j
    new.append(' '.join(array))
for s in range(1,number+1):
    mix=new[s]
    print(mix[1:])
            
