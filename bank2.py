class Result:
  '''Result class with three attributes success,message,value
  We can make two child classes that inherit from the Result class one for True and False outcomes for a withdrawal
  '''
  def __init__(self,success,message,value):
    self.success = success
    self.message = message
    self.value = value
    
class Ok(Result):
  def __init__(self,message,value):
      super().__init__(self,message,value) # inherites initialised attributes from Result class
      self.success  = True

class Error(Result):
  def __init__(self,message, value):
      super().__init__(self,message, value)
      self.success = False
    
class Bank:
  id = 1
  def __init__(self,balance):
    self.balance = balance
    self.id = Bank.id
    Bank.id+=1
    self.withdrawalHistoryList = []
    self.provider = 'Barclays Bank PLC'
    
  def withdrawal(self,amount):
    if (amount<=self.balance and amount>=0):
      self.balance-=amount
      print('Succesful')
      return Ok('Succesful Withdrawal',amount)
    
    else:
      return Error('Not enough funds for withdrawal',amount)
    
  def deposit(self,amount):
    '''Allows user to deposit money into account
    '''
    if amount<0:
      raise ValueError('Deposit must be greater than 0 dollars')
    
    else:
      self.balance+=amount
      
  def __repr__(self):
    return 'Current balance:' + str(self.balance)
  
  def withdrawalHistory(self):
    length = len(self.withdrawalHistoryList)
    return 'This account has made a total of' + ' ' + str(length) + ' ' + 'withdrawals'
  
  def showFunds(self):
    return self.balance
  
b = Bank(1000)
print(b.showFunds())
print(b.withdrawal(100).success)

class BasicAccount(Bank):
  def __init__(self, balance,threshold):
      super().__init__(balance)
      self.threshold = threshold
      
  def withdrawal(self, amount):
    if(self.balance-amount>= self.threshold):
      return super().withdrawal(amount)
    
    else:
      return 'Threshold has been reached you can no longer with draw'
print('--------')
b = BasicAccount(1000,500)
b.deposit(100)
print(b.withdrawal(700).success)
