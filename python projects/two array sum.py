def find(array1,array2,add):
    import time
    start=time.time()
    for i in range(len(array1)):
        res=add-array1[i]
        if res in array2:
            return True
            break
    else:
        print(time.time()-start)
        return False

def find2(array1,array2,add):
    import time
    start=time.time()
    var=True
    for i in range(len(array1)):
      for k in range(len(array2)):
      	if array1[i]+array2[k]==add:
      		return True
      		var=False
      		break
      if var==False:
      	break
    if var==True:
        print(time.time()-start)
        return False

print(find([x for x in range(1,13000)],[y for y in range(1,13000)],0))
