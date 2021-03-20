n=int(input())
for i in range(1,n+1):
    stars=['*']*i
    stars=' '.join(stars)
    string=(n-i)*' '+stars
    print(string)
