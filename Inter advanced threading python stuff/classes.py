

##a = Shape(sides=3, base=2, height=12)
#b = Shape(sides=4, length=2)
#print(a.area())
#print(b.area())

# I want `a` and `b` to be an instances of either of 'Square' or 'Triangle'
# depending on number of sides and also the `.area()` method to do the right
# thing. How do I do that without creating a Shape class with all the
# methods having a bunch of `if`s ? Here is one possibility

class Shape:
    def __new__(cls, sides, *args, **kwargs):
        if sides == 3:
            return Triangle(*args, **kwargs)
        else:
            return Square(*args, **kwargs)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length

class Shape_one:
    def __new__(self, sides,base=0,height=0):
        if sides==3:
            return self.makeTriangle(base,height)
        else:
            return self.makeSquare(base)
 
    def makeTriangle(base,height):
        class Triangle:
            def __init__(self,base,height):
                self.base=base
                self.height=height

            def area(self):
                return (self.base*self.height)/2
        return Triangle(base,height)
   
    def makeSquare(length):
        class Square:
            def __init__(self,length):
                self.length=length
            def area(self):
                return self.length*self.length
        return Square(length)
        
