string=input()
count=0
for i in range(len(string)):
    for c in range(len(string)-i):
        count=count+1
print(count)
