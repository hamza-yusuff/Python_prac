l=1
r=int(input())
x=int(input())
while l <= r: 
  
        mid = l + (r - l) // 2; 
        print(mid)  
        # Check if x is present at mid 
        if mid == x: 
            break
  
        # If x is greater, ignore left half 
        elif mid < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
