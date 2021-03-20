def make_sin(number):
    string_num=str(number)
    total_odd=0
    total_even=0
    for i in range(8):
        if i%2!=0:
            if 2*(int(string_num[i]))>10:
                num=2*(int(string_num[i]))
                num=int(str(num)[0])+int(str(num)[1])
            else:
                num=2*(int(string_num[i]))
            total_even=total_even+num
        else:
            total_odd=total_odd+int(string_num[i])
    total=10-int(str(total_even+total_odd)[1])
    return int(string_num+str(total))
    

        
