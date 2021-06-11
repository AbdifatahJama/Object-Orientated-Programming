import random
import locale as lc
lc.setlocale(lc.LC_ALL,'')

class Bank:
  id = 1
  def __init__(self):
      self.balance = 500
      self.withdrawalHistory = []
      self.id = Bank.id
      Bank.id+=1
    
  def __str__(self):
    '''string representation of object
    '''
    return 'Current Balance:' + str(self.balance)
  
  def deposit(self,amount = 0):
    '''Allows user to deposit money into account
    '''
    if amount<0:
      raise ValueError('Deposit must be greater than 0 dollars')
    
    else:
      self.balance+=amount
  
  def withdrawal(self,amount = 0):
    '''Allows user to withdraw money as long as they have enough funds
    '''
    if amount<= self.balance:
      self.balance-=amount
      '''If withdrawal succesfully goes through we want to log the history in a list
      '''
      self.withdrawalHistory.append(amount)
    elif amount>self.balance:
      raise ValueError('We cannot withdraw' + ' ' + str(amount) + ' ' + 'as you do not have sufficent funds' )
    
    else:
      raise ValueError('You must have sufficent funds for this')
    
  def showFunds(self):
    return self.balance
  
  def withDrawalHistory(self):
    length = len(self.withdrawalHistory)
    return 'This account has completed' + ' ' + str(length) + ' ' + 'withdrawals'
  
  
    
  
    
  
    
  
list = [Bank() for __ in range(10)]

for user in list:
  print('User:',user.id)
  print(user.showFunds())
  
# Next user id
print('Next:',Bank.id)

  


      