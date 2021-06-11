'''This script contains classes that will model different cars, the fuel in their tanks difference travelled 
'''
from math import perm
import random
from typing import overload

class Car:
  def __init__(self,fuel):
    self.__fuel = fuel
    self.mileage = 0
    self.warning = []
    
  def get_fuel(self):
    return self.__fuel
  
  def set_fuel(self,new_fuel):
    self.__fuel = new_fuel
    
  def travel(self,miles):
    if miles<10:
      self.__fuel-= 5
      
    elif miles>=10 and miles<15:
      self.__fuel-= 10
      
    elif miles>=15 and miles<25:
      self.__fuel-=15
      
    elif miles>=25 and miles<35:
      self.__fuel-=20
      
    else:
      self.__fuel-=35
      
  def refuel(self):
    '''Refuels tank back up to 100 litres
    '''
    print('Tank re filled back up to 100 litres')
    self.__fuel = 100
    
  def __getitem__(self,key):
    return self.warning[key]
  
  def __repr__(self):
    return 'Car has' + '' + str(self.__fuel) + 'litres of fuel in its tank'
  
  
class Race:
  def __init__(self,amount):
    self.amount = amount
    self.race_list = [Car(random.choice([50,100,80,90,120,150,200])) for __ in range(self.amount)]
    
  def race(self):
    for i in self.race_list:
      print(i.get_fuel())
      i.travel(10)
      print(i.get_fuel())
      print('--------.')
r = Race(5)
r.race()   
print('----------')
c = Car(100)
c.travel(100)
print(c.get_fuel())
c.refuel()
print(c.get_fuel())
c.travel(30)
print(c.get_fuel())
print(c)
















    
    
  