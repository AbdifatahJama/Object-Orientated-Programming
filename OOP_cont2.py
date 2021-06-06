'''
This file will continue from where 'OOP_Intro.py' ended off
'''
from math import sqrt
import random

# -> Product class 
globall = 'Global varaible'
class Product:
  '''
  This class is a product class
  '''
  def __init__(self,name = '',price = 0.0,discount = 0):
    self.retailer = 'Tesco'
    self.name = name
    self.price = price
    self.discount = discount
    print('Initialised')
    
  def informationOfProduct(self):
    '''This method prints out the objects attributes
    '''
    print(self.retailer,self.name,self.price,self.discount)
    
  def newPrice(self):
    '''This method calculates the new price
    '''
    return self.price - (self.price*self.discount/100)
    
p1 = Product('Pizza',1.50,10)
p2 = Product('Burger',1.90,5)
p3  = Product('Choclate',2.75,2)

listOfProducts = [p1,p2,p3]
for i in listOfProducts: # Iterates through each object in the list and returns new price based on discount percentage
  print(i.newPrice())
  
  
'''Double underscore methods are named under methods and a example of dunder methods that we have already used is __init__ method where everytime an object is created the init method is invoked


The __str__ dunder method is simalar as everytime an object is printed such as

class Animal:
  def __init__(self,name,color,breed):
    self.name = name
    self.color = color
    self.breed = breed
    
  def __str__(self):
    return 'You just called the __str__ method'
    
hence:
we can create an object such as:

dog = Animal('Derrick',brown,'Yorkshire terrier)
print(dog) ->>>>> Will return what is inside the __str__

Any time an object is printed the dunder methods(__str__/__repr__) are executed
returns a string output when object is used as a string within a print statement

__str__ and __repr__ are both dunder methods used to get string representations of an object(ie printing an object)
'''
class Rocket:
  def __init__(self,speed):
    self.altitude = 0
    self.speed = speed
    
  def moveUp(self):
    self.altitude+=1
    
  def __str__(self):
    '''String dunder method that returns string from an object.
    Convert object to a string. __repr__ should return an official 
    string representation of an object
    '''
    return 'Current altitude:' + str(self.altitude) 
  
  def __repr__(self):
    '''Simalar to __str__ returns string representation of object. Goal of __repr__ is to retuns a clear string representation of the object.
    
    As a dev we should aim to use __repr__ more as repr() computes the “official” string representation of an object (a representation that has all information about the object)
    '''
    return 'Rocket' +'(' + str(self.speed) + ')'
  
  def get_distance(self,other_rocket):
    '''Calculates the absoulute distance of two rocket altitudes
    '''
    return abs(self.altitude - other_rocket.altitude)
    

r1 = Rocket(5)
r1.moveUp() # increases altitude by an increment 1
r1.moveUp() # increases altitude by an increment 1
r1.moveUp() # increases altitude by an increment 1
print(r1.altitude)
print(r1) # object is converted to a string when object is printed


# -> Organising code 
'''
for clean precise code we would want to seperate impelementation of classes from the classes it self. We do this by separate files. 

1) Creating classes 
2) importing classes from the file
'''

class Rockets:
  def __init__(self,speed):
    self.altitude  = 0
    self.speed = speed
    self.x = 0 # distance moved horizontally
    
  
  def moveUp(self):
    self.altitude+=1
    self.x = random.randint(1,10)
    
  def __str__(self):
    return 'Current altitide of rocket is:' + str(self.altitude)
     
  
  def __repr__(self):
    return 'Rockets' + '(' + str(self.speed) + ')'
  
  def get_distance(self,other_rocket):
    # return abs(self.altitude - other_rocket.altitude)
    y = abs(self.altitude - other_rocket.altitude)
    x = abs(self.x - other_rocket.x)
    # Using to calculate distance between two points Pythagoros theorem
    return sqrt(x^2 + y^2)
  
  
    
  
  
  
  
r1 = Rockets(5)
r1.moveUp()
print(r1.altitude)


'''We can than implement the below code into a class
'''
class RocketBoard:
  def __init__(self,amount):
    self.amount = amount
    print(self.amount)
    self.listofRockets = [Rockets(random.randint(1,10)) for __ in range(self.amount)]
    
    for __ in range(100): # iterates for the number of items in the list so repeats 10 times
      index = random.randint(0,len(self.listofRockets)-1) # picks a random index 0-9
      self.listofRockets[index].moveUp() # uses the moveup function on the object
      
    for rocket in self.listofRockets:
      print(rocket)
      
  def __getitem__(self,key): # returns value within a list/dictionary. 
    '''Allows to index the object name and it will return an item within the list attribute containing rocket objects'''
    return self.listofRockets[key]
    
  def __setitem__(self,key,value): # __setitem__ accepts 3 argument self,key,value (index and value to set it to).
    '''Allows us to index the object name and set the object altitude attribute to a specific value: ie: objectName[0] = value
    '''
    self.listofRockets[key].altitude = value
    
 
# We can instatiate rocketboards which will invoke the __init__ method everytime an object is created
# However,we cannot access the atributes of the rocketboard as within the rocket class there is no self.attribute refering to the rocketboard object

# Hence without self the attributes will be local variables and cannot be accessed by the individual objects

# It is always common practise to use the self keyword within the __init__ method. So the attributtes can be accessed and manipulated by the object created from the class


'''A file that contains classes is called a module. If a file has mutiple long classes we can seperate each class into its own module.

Then we can import each class from their respective modules to combine them togethor

If classes are completely different and not linked you must/good practise to make different files/module
'''

# Using more dunder methods
'''__getitem__ and __setitem__ dunder methods set and get values within lists dictionaries and arrays
'''



  
  





    
    

    