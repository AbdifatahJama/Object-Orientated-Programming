'''The following script will be a tictactoe game that  utilises object orientated programming 
'''
import random
import time
class Game:
  Round = 1
  def __init__(self):
    self.gameOver = False
    self.roundOver = False
    self.computerChoice = ['r','p','s']
    # self.round = Game.Round
    # Game.Round+=1
    self.userScore = 0
    self.cpuScore = 0 
    self.round = 1
    
       
  def __str__(self):
    return 'Rock Paper Scissors class'
    
  def __getitem__(self,key):
    return self.computerChoice[key]
  
  def computerMove(self):
    return random.choice(self.computerChoice)
  
  def PlayerWin(self):
    self.userScore+=1
  
  def ComputerWin(self):
    self.cpuScore+=1
    
'''We can make a small dictionary that maps different options'''

beat = {
  'r':'p',
  's':'r',
  'p':'s'  
}

win = {
  'r':'s',
  's':'p',
  'p':'r'
}



  
def intro():
  print('ROCK PAPER SCISSORS GAME')

def play_Game():
  intro()
  g = Game()
  '''Loops as long as roundover evaulates to false'''
  while not g.roundOver:
    userChoice = input('Enter your choice rock,paper or scissors (r,p,s):')
    if userChoice.isalpha() and userChoice in g.computerChoice:
      print('Computer choosing ')
      
      '''checks combination using if elif statements[COULD BE OPTIMISED]
      '''
      computerChoice = g.computerMove()
      if userChoice == computerChoice:
        print('Draw')
      
      if userChoice == 'r' and computerChoice == 's':
        print('Player wins')
        g.PlayerWin()
        
      elif userChoice == 'r' and computerChoice == 'p':
        print('Computer wins')
        g.ComputerWin()
        
      elif userChoice == 's' and computerChoice == 'p':
        print('Player wins')
        g.PlayerWin()
        
      elif userChoice == 's' and computerChoice == 'r':
        print('Computer wins')
        g.ComputerWin()
        
      elif userChoice == 'p' and computerChoice == 'r':
        print('Player wins')
        g.PlayerWin()
        
      elif userChoice == 'p' and computerChoice == 's':
        print('Computer win')
        g.ComputerWin()
        
      '''Current scores'''
      print('You:',g.userScore)
      print('Computer:',g.cpuScore)
      
      '''Checks if player or computer score. If total score of 3 is reached a winner is produced'''
      if g.userScore == 3:
        print('You have won and beat the computer')
        g.roundOver = True
        
      elif g.cpuScore == 3:
        print('You have lost to the computer') 
        g.roundOver = True  
    else:
      '''Handles any invalid inputs'''
      print('INVALID INPUT: Enter rock paper scissors choice as r,p,s')
           
play_Game()

