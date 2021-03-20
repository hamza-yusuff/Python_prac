n=int(input())
s=input()
string=list(s)
c=0
while "c" in string and "d" in string and "e" in string and "o" in string:
    string.remove("c")
    string.remove("d")
    string.remove("e")
    string.remove("o")
    c=c+1
print(c)
