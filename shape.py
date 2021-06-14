'''This module will contain three classes of shapes were the area and volume can be calculated

1) Rectangle
2) Sqaure
3) Cube
4) Circle

Volume cannot be calculated for Rectangle and Sqaure as it is a 2D shape
'''

class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
    
  def Area(self):
    return self.width*self.height
  
class Sqaure(Rectangle):
  '''Sqaure inherites attributes and methods from rectangle
  '''
  def __init__(self,side1):
    super().__init__(side1,side1)
      
  '''We do not need to make another Area method as the inheritance works as self.width and self.height are equal'''
class Cube(Sqaure):
  '''Inherites from sqaure class as cube is made up mutiple sqaures. Hence each side has the legnth 
  '''
  def Area(self):
      return super().Area()*6
    
  def Volume(self):
    return super().Area()*self.width
  
class SqaureBasedPyramid(Sqaure):
  def __init__(self, side1,vertical_height):
      super().__init__(side1)
      self.vertical = vertical_height
      
  def Area(self):
    pass
  
  def Volume(self):
    return (super().Area()) * self.vertical/3
  
  
class RectangleBasedPyramid(Rectangle):
  def __init__(self, width, height,vertical_height):
      super().__init__(width, height)
      self.vertical_height = vertical_height
      
  
  def Volume(self):
    '''Calculating volume using inheritance, Area method is part of what is used to calculate volume rectangle based pyramid
    '''
    return super().Area()*self.vertical_height/3

c = Cube(2)
print(c.Area())
print('------------')
print(c.Volume())


s = Sqaure(10)
print(s.Area())


pryamid = SqaureBasedPyramid(5,10)
print(pryamid.Volume())

rc = RectangleBasedPyramid(5,3,5)
print(rc.Volume())


class Cubes:
  '''As cube has sqaures we can use assocation with the sqaure class.
  '''
  def __init__(self,Sqaure):
    self.sqaure = Sqaure
    
  def Area(self):
    return self.sqaure.Area()*6
  def Volume(self):
    return self.sqaure.height**3
    
print('=========')
c = Cubes(Sqaure(5))
print(c.Area())
print(c.Volume())
