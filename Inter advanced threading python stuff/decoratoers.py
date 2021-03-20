import time
def func(f):
    def wrapper(*args,**kwargs):
        f(*args,**kwargs)
        print("works")
    return wrapper

@func
def hello():
    print('hello world')

@func
def loops(x):
    for i in range(x):
        pass


def timer(f):
    def wrapper(*args,**kwargs):
        start=time.time()
        f(*args,**kwargs)
        print(time.time()-start)
    return wrapper
username=input("enter username")
password=input("enter password")

def valid(f):
    def wrapper(*args,**kwargs):
        if username=="hamza" and password=="123":
            return f(*args,**kwargs)
        else:
            return None
    return wrapper

@timer
@valid
def loops(x,y):
    print(pow(x,y))
