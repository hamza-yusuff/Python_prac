stack=[]
mstack=[-1]
for i in range(int(input())):
     s=list(map(int,input().split()))
     if s[0]==1:
         stack.append(s[1])
         if s[1]>mstack[-1]:
             mstack.append(s[1])
         else:
             mstack.append(mstack[-1])
     elif s[0]==2:
         stack.pop()
         mstack.pop()
     elif s[0]==3:
         print(mstack[-1])
         
         
