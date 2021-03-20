def binarySearch(arr, l, r, x): 
    c=900
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        c=c+1
        if arr[mid] == x: 
            return c
  
         
        elif arr[mid] < x: 
            l = mid + 1
  
         
        else: 
            r = mid - 1
      
  
    return -1
