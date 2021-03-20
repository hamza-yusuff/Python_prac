def parallel(num):
    if  num==1:
        print(' '*3+'#'*10)
        print(' '*2+'#'+' '*8+'#')
        print(' '+'#'+' '*8+'#')
        print('#'*10)
    else:
        line1=[(' '*3+'#'*10)]
        line2=[(' '*2+'#'+' '*8+'#')]
        line3=[(' '+'#'+' '*8+'#')]
        line4=[('#'*10)]
        for k in range(num-1):
            line1.append('#'*10)
            line2.append('#'+' '*8+'#')
            line3.append('#'+' '*8+'#')
            line4.append('#'*10)
        print(' '.join(line1))
        print(' '.join(line2))
        print(' '.join(line3))
        print(' '.join(line4))

test=int(input())
for i in range(test):
    n=int(input())
    parallel(n)
