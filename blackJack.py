'''This script will model the famous game of blackjack using object orientated programming.Using object orientated programming will hopefully make the modelling of this simpler'''
import random
import csv
import numpy as np

class Player:
  id = 1
  def __init__(self):
    self.score = 0
    # Players have cards so we can use assocation
    self.id = Player.id
    Player.id+=1
    self.wins = 0
    self.cards = Cards()
    
  def start(self):
    
    '''Each player is given two random cards'''
    for __ in range(2):
      self.score+=self.cards.pickUp()
      
  def hit(self):
    self.score+=self.cards.pickUp()

  def stand(self):
    pass
  
  def busted(self):
    self.score = 0
    
  def win(self):
    self.wins+=1
    
  def __repr__(self):
    return 'Player Value:' + str(self.score)
  
class Dealer(Player):
  '''Dealer is very simalar to a player but has some differences hence, we will inherit player class'''
  
  def __repr__(self):
    return 'Dealer Value:' + str(self.score) 
  
  '''Dealer starts the game slightly differently to the other players, Dealer starts game only knowing the value of one card whereas the other card is placed face down and only revealed after all the other players decide to hit or stand'''
  
  def start(self):
    self.score+=self.cards.pickUp()
  
    

class Game:
  '''Game class'''
  def __init__(self):
    self.GAMENAME = 'BlackJack/21'
    self.round = 1
    self.gameOver = False
    self.roundOver = False
    # Game has cards so we can use assoscation/compisition
    self.cards = Cards()
    
class Cards:
  def __init__(self):
    self.FaceValue = [1,2,3,4,5,6,7,8,9,10] # Face value cards keep their value
    self.specialCards = {
      'king':10,
      'queen':10,
      'jack':10,
      'ace':[1,11]
    }
    
  def pickUp(self):
    self.list = [self.FaceValue,self.specialCards]
    item = random.choice(self.list)
    if isinstance(item,list):
      value = random.choice(item) # Gets random card with face value
      return value

      
    elif isinstance(item,dict):
      key = random.choice(list(item))
      if key == 'ace':
        '''When an ace is given an ace can take two values which is expressed as an array'''
        value = np.array([1,11])
        return value
      
      else:
        value = item[key]
        return value
      
# c = Cards()
# c.pickUp()

# p = Player()
# p.start()
# print(p.score)
# print('------')
# print(p.pickFromStack())


def intro():
  print('Welcome, you are now playing BlackJack or sometimes known as 21\nThere are few rules that must be explained first:\n1) This game involves up to 5 players and one dealer to allow the game to flow with ease\n2) To start each player and dealer will be given 2 cards from the shuffled stack\n3) The aim is to have a collection of cards that are eqaul or less than 21\n4) A collection of cards that sum greater than 21 is known as busting\n5) Any busted players from the game are eliminated')
  
def play_Game():
  g = Game()
  intro()
  while not g.gameOver:
    while not g.roundOver:
      howManyPlayers = input('How many players will be in this game excluding the defualt dealer:')
      if howManyPlayers.isdigit():
        howManyPlayers = int(howManyPlayers)
        if howManyPlayers<=5:
          playerList = [Player() for __ in range(howManyPlayers)]
          playerList.append(Dealer())
          break
          
        else:
          print('Maximum players for this game is 5 players exluding the dealer. Please Try again and satisfy this condition')
        
        
      else:
        print('Invalid input. Try again')
    
    print('Cards being distributed to each player(Two each)')
    i = 1
    for player in playerList:
      '''Iterates through each player and Dealer and distributes two cards to each'''
      print('Player',i)
      player.start()
      i+=1
    i = 1
    for player in playerList:
      '''Shows the total of the two cards for each player and dealer'''
      print('Player'+ ' ' + str(i) + ' ' + 'card total')
      print(player.score)
      i+=1
    print(playerList)
      
    'We then want to iterate through each player and ask if they want to hit or stand'
    for player in playerList[0:len(playerList)-1]:
      print('Player ID:',player.id)
      while True:
        choice = input('Do you want to hit or stand(h/s):')
        if choice == 'h':
          player.hit()
          print('Player ID' + ' ' + str(player.id) + ' ' + 'current score:' + str(player.score) )
          
        elif choice == 's':
          print('Player ID:' + ' ' + str(player.id) + ' ' + 'has stood' )
          print('Player ID' + ' ' + str(player.id) + ' ' + 'stood score:' + str(player.score) )
          break
        
        else:
          print('Enter valid input (h - hit or s - stand)')
            
    '''We then want to reveal the Dealer card as they must hit their second card'''
    playerList[len(playerList)-1].hit() # Dealer second card
    print('DEALER PICK UP CHOICES')
    while True: # Loops if two cards are less than 16 so must hit until greater than 16
      if isinstance(playerList[len(playerList)-1].score,int) and playerList[len(playerList)-1].score<=16:
        '''Checks if Dealer score is an integer or within a numpy array'''
        print('Integer')
        playerList[len(playerList)-1].hit()
        
      elif isinstance(playerList[len(playerList)-1].score,np.ndarray):
        '''BAD ASSUMPTION HERE, need to check the values of the cards before hitting. ST SOLUTION SO FAR'''
        print('Array')
        if playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1]<=16:
          playerList[len(playerList)-1].hit() 
          
        else:
          break
      
      else:
        print('Dealer does not need to hit as score is already 17 or higher')
        break
    print('Final Scores') 
    print(playerList)
    print('REACHED')
    '''After all parties within the gane have either stood or held we can compare each players score with the dealers score.
    
    We iterate through the player in playerList [0:4] and .score attributes
    
    '''
    
    for player in playerList[0:5]:
      if isinstance(player.score,int):
        if isinstance(playerList[len(playerList)-1].score,int):
          if (player.score<=21) and (player.score>playerList[len(playerList)-1].score):
            player.win()
            print('Player' + ' ' + str(player.id) + ' ' + 'has won')
            
          elif (player.score<=21) and (playerList[len(playerList)-1].score>21):
            player.win()
            
          elif (player.score<=21) and (player.score<playerList[len(playerList)-1].score) :
            print('Player' + ' ' + str(player.id) + ' ' + 'has lost to the dealer')
            
          elif (player.score==21) and (player.score>playerList[len(playerList)-1].score):
            player.win()
            print('Player' + ' ' + str(player.id) + ' ' + 'BlackJack')
            
          else:
            print('Player' + ' ' + str(player.id) + ' ' + 'has busted')
              

        
        elif isinstance(playerList[len(playerList)-1].score,np.ndarray):
          if (player.score<=21) and (player.score>playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1]):
            player.win() # increments win attribute by 1
            print('Player' + ' ' + str(player.id) + ' ' + 'has won')
            
          elif (player.score<=21) and (player.score<playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1]):
            print('Player' + ' ' + str(player.id) + ' ' + 'has lost to the dealer')
            
          elif (player.score==21) and (player.score>playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1]):
            player.win()
            print('Player' + ' ' + str(player.id) + ' ' + 'BlackJack')
            
            
          elif (player.score<=21) and (playerList[len(playerList)-1].score[0]>21 and playerList[len(playerList)-1].score[1]>21):
            player.win()
            
            
          else:
            print('Player' + ' ' + str(player.id) + ' ' + 'has busted')      
          
      
      elif isinstance(player.score,np.ndarray):
         if isinstance(playerList[len(playerList)-1].score,int):
           if (player.score[0]<=21 or player.score[1]<=21) and ((player.score[0] or player.score[1])>playerList[len(playerList)-1].score):
             player.win()
             
           elif  (player.score[0]<=21 or player.score[1]<=21) and ((player.score[0] or player.score[1])<playerList[len(playerList)-1].score):
             print('Player' + ' ' + str(player.id) + ' ' + 'has lost to the dealer')
             
             
           elif (player.score[0]==21 or player.score[1]==21) and ((player.score[0] or player.score[1])>playerList[len(playerList)-1].score):
             player.win()
             print('Player' + ' ' + str(player.id) + ' ' + 'BlackJack')
             
            
           elif (player.score[0]<=21 or player.score[1]<=21) and (playerList[len(playerList)-1].score>21):
             player.win()
             print('Player' + ' ' + str(player.id) + ' ' + 'has won')
             
           else:
             print('Player' + ' ' + str(player.id) + ' ' + 'has busted')  
             
             
         elif isinstance(playerList[len(playerList)-1].score,np.ndarray):
           if (player.score[0]<=21 or player.score[1]<=21) and ((player.score[0] or player.score[1])>(playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1])):
             player.win()
             print('Player' + ' ' + str(player.id) + ' ' + 'has won')
            
           elif (player.score[0]<=21 or player.score[1]<=21) and ((player.score[0] or player.score[1])<(playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1])):
             print('Player' + ' ' + str(player.id) + ' ' + 'has lost to the dealer')
             
           elif (player.score[0]==21 or player.score[1]==21) and ((player.score[0] or player.score[1])>(playerList[len(playerList)-1].score[0] or playerList[len(playerList)-1].score[1])):
             print('Player' + ' ' + str(player.id) + ' ' + 'BlackJack')
             
           elif (player.score[0]<=21 or player.score[1]<=21) and (playerList[len(playerList)-1].score[0]>21 and playerList[len(playerList)-1].score[1]>21):
             player.win()
             print('Player' + ' ' + str(player.id) + ' ' + 'has won')
             
           else:
             print('Player' + ' ' + str(player.id) + ' ' + 'has busted') 
             
             
    g.gameOver = True
                        
          
      
play_Game()

  