class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self,point):
        return print(Point(point.x+self.x,
                     point.y+self.y))

    
        
