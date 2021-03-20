#Key Takeaways:
##Instance methods need a class instance and can access the instance through self
##Class methods dont need a class instance. They cannt
# acces the instance (self) but have access to class itself
# via cls
##Static methods dont have access to cls or self. They work
# like regular functions but belong to class's namespace




class medium():
    objects=0
    def __init__(self,name,radius=0,shape=None,area=False,perimeter=False,objects=1):
        self.name=name
        self.radius=radius
        self.shape=shape
        self.area=area
        self.perimeter=perimeter
        self.objects=objects
    
    @classmethod
    def objects_created(cls):
        cls.objects=cls.objects+1
        print("number of objects",cls.objects)

    def output_attributes(self):
        if not self.shape:
            print("No shape name")
            print("Author name {}".format(self.name))
        else:
            if self.area and not self.perimeter:
                return self.calculate_area(self.shape,self.radius)
            elif not self.area and self.perimeter:
                return self.calculate_perimeter(self.shape,self.radius)
            elif self.area and self.perimeter:
                return self.calculate_both(self.shape,self.radius)
            else:
                print('Shape :', self.shape)

    @staticmethod
    def calculate_area(shape,radius):
        if shape=='rectangle':
            return "Not possible"
        elif shape=='circle':
            return radius*radius*3.14
        elif shape=='sphere':
            return pow(radius,3)*(4/3)*3.14
        elif shape=='sqaure':
            return radius*radius

    @staticmethod
    def calculate_perimeter(shape,radius):
        if shape=='rectangle':
            return "Not possible"
        elif shape=='circle':
            return 2*3.14*radius
        elif shape=='sphere':
            return 0.5*pow(radius,3)*(4/3)*3.14
        elif shape=='square':
            return radius*4
        else:
            return "go to hell"

    @staticmethod
    def calculate_both(shape,radius):
        print("area :" , self.calculate_area(shape,radius), "perimeter :", self.calculate_perimeter(shape,radius))
    
            
    
        
