# Introduction to Object Oriented Programming

# OOP is programming which is oriented around objects
# Up to this point we have been using procedural programming where the script is ran from top to bottom 

# For more complicated projects which requires more thinking OOP is an advantage
# OOP allows medium/larger project easier to comprehend

''''
  Objects - Objects are containers that store varaibles(Attributes) and Functions(methods) 
            A simple example is that a dog is an object which has:
            a name
            a height
            a weight
            Methods - Run,bark,move tail etc
            
            
  Class - a class is a blueprint of objects
          - a class defines any attributes or methods that will characterize any object that is instantiated from this class
          Hence, it is often said an object is an instance of a class (hence the word instantiate)
          
          Always start of class with UPPERCASE so it is not mixed up with methods

'''

# We want to make a class of users that we can instatiate
age = 1
class User:
  age = 0
  height = 20
  
u1 = User()
print(u1.age)
print('Global Age:',age)
print(u1) # when you print the object it shows different addresses 'at 0x000002..

u2 = User() # when you print the object it shows different addresses 'at 0x0000022E..
# Hence we do something to one object it will not affect the other object
print(u2)

# We can create attributes within the class or outside of the class using the .method
u1.height = 15
print(u1.height)
# However when we run (print(u2.height)) --> there will be a an attribute error as user 2 does not have height attribute. Hence to set a age to both object we set attributes within the class
print('Jessica Height',u2.height)

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Exercise 1 ---> Create a Monitor class and subsequently different object instances based of the monitor class

class Monitor:
  height = 5
  width = 9
  Dwidth = 11
  weight = 5.6
  
m1 = Monitor()
print('Monitor 1 Object')
print(m1.height)
print(m1.width)
print(m1.Dwidth)
print(m1.weight)
m1.height = 6 # ---> changes height attribute of m1 object to 6
print(m1.height) # Hence m1 height attribute prints out 6
'''
  Creating a method is one of the most important thigns within a class along with attributes
  
  self - Everytime a method is created within a class the first argument within the method is the object it self which is assigned to self. This allows the object to access attributes of the object
  
  To access the object attributtes the self keyword is key. self.height, self.weight
  
  if self keyword is not used it will access the global varaible of the attribute if one exists
  
  To access a attribute within an object the self keyword must be used. If not the script will search for the varaible at global scope level
  
  age and self.age could be two different numbers
'''

# Creating normal function

def print_age(age,name):
  print(age,name)
  
name = 'Jonathan'
print_age(50,name)

age = 75 # -> Global variable
class Users:
  age = 5
  name = ''
  
  def show_age(self,additional_message):
    print(self.name,self.age,additional_message) # prints out the objects attribute along with the methods argument of additional_message which is now a required argument for the method to work. Self is not needed for additonal message as it is not a attribute
      

a1 = Users()
a1.name = 'Stephen'
print(a1.show_age('Addtional message'))

a2 = Users()
a2.name = 'Micheal'

print(a2.show_age('something'))

a3 = Users()
a3.name = 'Jackson' # -> changes a3 object attribute from the class blue print
print(a3.show_age('message'))

# Exercise 2 - > setting a class with attributes,methods and creating object from that
z = 'Global scope(variable outside of class)'
class Student:
  name = ''
  School = 'UCLA'
  Year = 2021
  
  def reveal_information(self):
    print(self.name,self.School,self.Year,z)
    
# Creating object
s1 = Student()
s1.name = 'Clint' # -> resets object attribute from an empty string to string name 'clint'

print(s1.reveal_information())

s2 = Student()
s2.name = 'Nikola'

print(s2.reveal_information())

listofStudents = [s1,s2] # -> puts s1 and s2 objects into a list
for i in listofStudents: # -> iterates through the list and then prints out the name attribute
  print(i.name)
  
'''
So far we have been setting some attributes such as name to an empty string in a class then overiding it using the object.name = 'name' method.

This is not common practise and it is better practice to initialise attributes in classes using the init function (initialisation function). Also called a constructor

Every time an object is created the init method is always invoked. This can proven if we stick a print statement within the init method. Everytime we make an object the print statement within the init is invoked

Hence, when we create an object we invoke everything within the init method
'''  

class Player:
  age = 6
  name = ''
  def __init__(self,name,age): # -> intialises attributes
    self.name = name # name is set to the self.name object attribute
    self.age = age   # age is set to the self.age object attribute
    self.newVaraibleThatIHaveCreated = 435
    print('init method has been invoked')
    print(self.name)
    print(self.age)
    print('------------------')
    
  def information(self):
    print(self.name,self.age,self.newVaraibleThatIHaveCreated)
    
    
p1 = Player('Jack',21) # -> Object called p1 instantiated and invokes init method/constructor
p2 = Player('Holly',24) # -> Object called p2 instantiated and invokes init method/constructor
p3 = Player('Stan',29) # -> Object called p3 instantiated and invokes init method/constructor


p1.information() # -> calls method within object/class

# Exercise 3 - Create a rocket class 
import random
class Rocket:
  def __init__(self):
    self.altitude = 0
    
  def moveUp(self):
    self.altitude+= random.randint(1,100)
    
# we want to make 500 instances of rockets

listofRockets = [Rocket() for i in range(500)] # - > using list comprehension to produce a list with 500 rocket objects
print(len(listofRockets))

for i in listofRockets: # loops through each item within the list and sets each object to i
  i.moveUp() # calls moveUp method that manipulates self.altitude
  print(i.altitude) # prints out new altitude
  
# -> We can take this a step up and introduce a speed attribute and depending on the speed of the rocket it changes the altitude
# -> We create whole new  class called Rockets so we dont change the above exercise 

class Rockets:
  '''
  Represents a rocket with set altitude and speed and how the altitude changes with speed
  '''
  # Above shows a docstring that allows a user/dev to know what a specific class is used for
  def __init__(self,speed):
    self.altitude = 0 # -> initialises objects altitude to zero
    self.speed = speed #-> intialises speed input as objects speed(self.speed)
    
  def moveUp(self): # method uses if statements of the objects speed to determine altitude
    '''Moves rocket depending on objects speed
    '''
    if self.speed == 1: 
      self.altitude+=1
      
    elif self.speed > 1 and self.speed<=50:
      self.altitude +=10
      
    else:
      self.altitude+=100
      
      
list = [Rockets(random.randint(1,100)) for i in range(100)]

for i in list:
  i.moveUp()
  print(i.speed)
  print(i.altitude)
  
  
  
  





    





    
    





  