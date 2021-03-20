def pipelines(file_name):
    lines = (line for line in open(file_name))
    list_line = (s.split() for s in lines)
    cols = next(list_line)
    company_dicts=(dict(zip(cols,data)) for data in list_line)
    funding= (int(company_dict["raisedAmt"])
              for company_dict in company_dicts
              if company_dict["round"] === "a")
    total_series_a =sum(funding)







def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row
#csv_gen =(row for row in open(file_name))

def infinite_sequence():
    num=0
    while True:
        yield num
        num +=1

#list comprehension -->
nums=[num**2 for num in range(1000)]

#generator comprehension-->
num_gc=(num**2 for num in range(1000))

def multi_yield():
    first="first one"
    yield first
    second="second one"
    yield second

h=multi_yield()

#three generator methods --> send(), throw(), close()
def func():
    i=1
    while i != None:
        num = (yield i)
        
        if num is not None and len(str(num))>2:
            print(num)
            i=num
        i=i+1
	


def new():
    f=func()
    for n in f:
        if  n>25:
            f.send(n//10)

def countdown(n):
    print("counting down")
    while n>0:
        yield n
        n=n-1
    print("done")

def checkval():
    
    while True:
        num=(yield)
        print(num)
        if num is not None and str(num) in "123456789":
            print("Inside")
while True:
    
    numbers=input()
    f=checkval()
    f.send(None)
    if numbers != None:
        if int(numbers)>=1000:
            print("close")
            f.close()
            break
        else:
            
            f.send(numbers)
            

    
        
    
