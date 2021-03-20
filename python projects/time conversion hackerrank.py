time=input()
if time[len(time)-2:]=="PM" and time[:2]!="12":
    hour=int(time[:2])+12
    print(str(hour)+time[2:len(time)-2])
elif time[len(time)-2:]=="AM" and time[:2]!="12":
    print(time[:len(time)-2])
elif time[len(time)-2:]=="PM" and time[:2]=="12":
    print(time[:len(time)-2])
elif time[len(time)-2:]=="AM" and time[:2]=="12":
    print("00"+time[2:len(time)-2])
    
