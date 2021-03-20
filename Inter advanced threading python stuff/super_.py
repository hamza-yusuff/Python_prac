class Land:
  def __init__(self,price,location,length,width):
    self.location=location
    self.length=length
    self.width=width
    self.price=price

  def area(self):
    return self.length*self.width

  def perimeter(self):
    return 2*self.length*2*self.width

class citizen:
  def __init__(self,fname,lname,number):
    self.fname=fname
    self.lname=lname
    self.number=number

  def __str__(self):
    return "{} {}".format(self.fname,self.lname)

  def details(self):
    return self.__str__()+" "+str(self.number)

class Buyer(citizen):
  def __init__(self,fname,lname,number,money,bought=False):
    self.money=money
    self.bought=bought
    super().__init__(fname,lname,number)

  def hasbought(self,p):
    if self.money-p>=0:
      self.bought=True
    return self.bought


class Seller(Land,citizen):
  def __init__(self,fname,lname,number,set_price,address,length,width,sold=False):
    self.sold=sold
    self.fname=fname
    self.lname=lname
    self.number=number
    super().__init__(set_price,address,length,width)

  def hassold(self,p):
    if self.price-p<=0:
      self.sold=True
    return self.sold

class property:
  def __init__(self,seller,buyer,verdict=False):
    self.seller=seller
    self.buyer=buyer
    self.verdict=verdict

  def whose_property(self):
    owner_money=self.buyer.money
    seller_money=self.seller.price
    if self.buyer.hasbought(seller_money) and self.seller.hassold(owner_money):
      return self.buyer.__str__()
    return self.seller.__str__()
    




























class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

# Mammal inherits Animal
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a mammal.')
    super().__init__(mammalName)
    
# CannotFly inherits Mammal
class CannotFly(Mammal):
  def __init__(self, mammalThatCantFly):
    print(mammalThatCantFly, "cannot fly.")
    super().__init__(mammalThatCantFly)

# CannotSwim inherits Mammal
class CannotSwim(Mammal):
  def __init__(self, mammalThatCantSwim):
    print(mammalThatCantSwim, "cannot swim.")
    super().__init__(mammalThatCantSwim)

# Cat inherits CannotSwim and CannotFly
class Cat(CannotSwim, CannotFly):
  def __init__(self):
    print('I am a cat.');
    super().__init__('Cat')

# Driver code
cat = Cat()
print('')
bat = CannotSwim('Bat')


