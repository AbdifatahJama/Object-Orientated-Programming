'''Using OOP to create a business program using a multi tier architecture 

Most applications have three distinct tiers:

Presentation tier - Handles the users interface
Database tier - Handles the users data and stores within tables inside a database
Business tier - Acts as an interface between the database and presentation class that tells users their credit,busineess role,discounts and available products

There are many advantages to using OOP to divide sections of a program into classes. 
One reason is a class can be swapped out such as the presentation tier to use a GUI interface rather than console based without affecting other classes such as database and business classes
'''

'''Shopping cart'''


class Products:
  def __init__(self,name = '',price = 0,discount_percent = 0):
    self.name = name
    self.price = price
    self.discount = discount_percent
  
  def getDiscountAmount(self):
    '''Gets discount amount that is subtracted from original price'''
    return self.price*(self.discount/100)
  
  def getDiscountPrice(self):
    return self.price - self.getDiscountAmount()


class Lineitem:
  def __init__(self,product,qauntity = 1):
    self.qauntity = qauntity
    self.product = product # Lineitem has a product so composition so composition is used 
    
  def get_total(self):
    return self.product.getDiscountPrice()*self.qauntity
  
  def __repr__(self):
    return str(self.product.name)
  
class Cart:
  '''Cart stores product in line item'''
  def __init__(self):
    self.list = []
    
  def getList(self):
    return self.list
  
  def addItem(self,item):
    '''Adds an item into the cart list'''
    self.list.append(item)
  
  def removeItem(self,index):
    '''Removes an item into the cart list'''
    self.list.pop(index)
    
  def itemCount(self):
    return len(self.list)
  
  def final_total(self):
    total = 0
    for item in self.list:
      '''Iterates through each Lineitem in cart list'''
      total+=item.get_total()
      
    return total
  
  
  
      
      
    
  
    
  
  