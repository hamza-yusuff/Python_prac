for i in range(int(input())):
    s=input()
    v="aeiouAEIOU"
    for k in range(len(v)):
        if v[k] in s:
            print("Yes")
            break
    else:
        print("No")
    
