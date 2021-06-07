import random

class Die:
  '''Individual Die class
  '''
  def __init__(self):
    self.value = 1
    
  def roll(self):
    self.value = random.randint(1,6)
    
  def __repr__(self):
    # return 'Die' + '(' + str(self.value) + ')'
    return 'Die Value:' +  str(self.value)
  
  def get_diiference(self,last_die):
    '''Function finds difference between the two die
    '''
    return abs(self.value - last_die.value)
  

  
class Dice:
  '''Stores mutiple Die object and rolls them all once
  '''
  def __init__(self,rolls):
    self.rolls = rolls
    self.list = [Die() for __ in range(self.rolls)]
    
  def rollDie(self):
    for die in self.list:
      die.roll()
      
    for die in self.list:
      print(die) # Die object has __repr__ method that shows object in string representation. In this case when the object is printed it shows the value of the die
      
  def __getitem__(self,key):
    '''Allows us to access list attribute by simply using the object name and index. ObjectName[index]. This returns an item within the list
    '''
    return self.list[key]
  
  def __setitem__(self,key,value):
    '''Allows us to set value attribute of the die object within the list to be changed
    '''
    self.list[key].value = value
    
  def sum(self):
    '''Iterates through list and finds value of each die object finds the sum using a for loop
    '''
    total = 0
    for i in self.list:
      total += i.value
    print(total)
    
d = Dice(10)
d.rollDie()
print()
d[0] = 10 # uses the __setitem__ to change the 0th index item within a list which is a die object value attribute to 10
print(d[0].value)

print(d[1].get_diiference(d[2])) # Using __getitem__() dunder method to get Die object item within list d[1] would be equivalent to self
print()
d.sum()
