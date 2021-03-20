class car:
    def __init__(self,name,color):
        self.n=name
        self.c=color
    def start(self):
        print("starting", self.n, self.c)
my_car=car("allion","red")
print(my_car.n, my_car.c)
my_car.start()
