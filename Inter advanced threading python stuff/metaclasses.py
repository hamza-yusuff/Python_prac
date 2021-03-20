










#using __new__
class players(object):
    _number=0
    def __new__(cls, *args,**kwargs):
        instance=object.__new__(players)
        if cls._number==2:
            return None
        else:
            cls._number+=1
            return instance

    def __init__(self,fname,lname,score):
        self.fname=fname
        self.lname=lname
        self.score=score

    def __str__(self):
        return f"{self.fname} {self.lname}"









class Foo:
    def show(self):
        print('hi')
def add_attribute(self):
    self.z=9
    print(self.z+1)
Test=type('Test',(Foo,),{'x':5,'add_attribute':add_attribute})
t=Test()
t.wy="hello"
t.add_attribute()
print(Test.x)


class foo:
    def __new__(cls, *args, **kwargs):
        instance = super(foo, cls).__new__(cls)
        print(instance)
        return instance
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def bar(self):
        pass
