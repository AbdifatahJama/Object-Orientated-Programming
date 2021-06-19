'''This script will use inhertitance to produce linked employee classes

1) Manager
2) Executive
3) Factory Worker
4) Admin
5) Store Worker
6) Intern
'''

class Employee:
  '''This can be an abstract class as we dont really want to instatiate this class only inherit'''
  def __init__(self,name = '',age = 0):
    self.name = name
    self.age = age
    
  def __repr__(self):
    return str(self.name) + ' ' + str(self.age)
  
class Manager(Employee):
  def __init__(self, name, age,salary):
      super().__init__(name, age)
      self.salary = salary
      
  def getSalary(self):
    return self.salary
  

class HourlyEmployee(Employee):
  def __init__(self, name, age,hours,hourlyPay):
      super().__init__(name, age)
      self.hours = hours # Weekly hours
      self.hourlyPay = hourlyPay
      
  def getSalary(self):
    '''Calculates weekly salary'''
    return self.hours*self.hourlyPay
  
class CommisionEmployee(Manager):
  def __init__(self, name, age, salary,commision):
      super().__init__(name, age, salary)
      self.commision = commision
      
  def getSalary(self):
      return super().getSalary() + self.commision
    
    
manager = Manager('Abdifatah',20,20000)
Hourly_Employee = HourlyEmployee('James',21,30,9.50)
commision_Employee = CommisionEmployee('Jack',24,15000,204.90)

class PayRoll:
  def __init__(self):
    self.list = [manager,Hourly_Employee,commision_Employee]
    
  def pay(self):
    for i in self.list:
      print(i)
      print(i.getSalary())
      print('-----------')
      
p = PayRoll()
p.pay()


'''The Class Explosion Problem'''

class Managers(Manager):
  def work(self,hours):
    print('Manager' + ' ' + 'screams and shouts for' + ' ' + str(hours))
    
class Secatary(HourlyEmployee):
  def work(self,hours):
    print('Secatary works for' + ' ' + str(hours) + ' ' + 'in the office, she makes' + ' ' + str(super().getSalary()))
    
    
mangers = Managers('Jones',29,19000)
sec = Secatary('Jessica',32,10,32.50)
sec.work(5)

class StoreWorker(CommisionEmployee):
  def work(self,hours):
    print('Store worker gets a salary that consists of a set salary plus commision based on external targets.' + ' ' + 'This store worker worked' + ' ' + str(hours) + ' ' + 'hours')


store = StoreWorker('James',26,19000,215.75)
store.work(10)

class ProductivitySystem:
  def track(self,employees,hours):
    for employee in employees:
      print('Name:',employee.name)
      print('Productivity:',employee.work(hours))
      print('------------------')
      
listOfEmployees = [mangers,sec,store]
p = ProductivitySystem()
p.track(listOfEmployees,10)

'''Mutiple inheritance

can be used in classes that inherit different interfaces from different classes
Such as TemporarySecretary peforms the role of secatary but is a hourlyEmployee
'''

class TemporarySecretary(Secatary): # Inherites Secatary that inherites from HourlyEmployee
  pass


TSY = TemporarySecretary('Abdi',28,8,9.50)
print(TSY.getSalary())
      
  



    