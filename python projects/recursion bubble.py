def bubble(arr,size,i):
    count = 0
    for i in range(size-i):
        if arr[i]>arr[i+1]:
            temp=arr[i+1]
            arr[i+1]=arr[i]
            arr[i]=temp
            count=1
    if count==0:
        return arr
    else:
        i=i+1
        return bubble(arr,size,i)
num=[1,3,2,5,4,6]
print(bubble(num,len(num),1))
