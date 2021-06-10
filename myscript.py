from OOP_cont2 import Rocket, Rockets,RocketBoard

# board = RocketBoard(10)
# print('-----------')
# board1 = RocketBoard(20)
# print(board1.listofRockets[19].altitude) #-> object uses the self.listofRockets attribute which is equal to a list containing Rocket objects. We can get a specific rocket object and find the altitude using one of the Rocket class atribute

'''A file that contains classes is called a module. If a file has mutiple long classes we can seperate each class into its own module.

Then we can import each class from their respective modules to combine them togethor

If classes are completely different and not linked you must/good practise to make different files/module
'''
board = RocketBoard(11)
print('---------')
board[0]
print(type(board[0])) #-> Rocket object as it accesses item within list that contains rocket objects

board1 = RocketBoard(5)

print(type(board1[0]))

# print(board1[0].get_distance(board1[1]))
print(board1[0].altitude) # -> random x distance rocket attribute

# Finding distance between 2 points using pythagoros theorom

print(board1[1].get_distance(board1[4])) # uses rocket method 'get_distance()' to get distance between two points

# Using static method to calculate distance bewteen two points
# Static methods use the class name when calling a method as it is bounded to a class

board2 = RocketBoard(10)
print('-----------')
print(board2[0])
print(board2[3])
print(RocketBoard.get_distance(board2[0],board2[3]))

# As method is static it not bounded to class or object. Hence, we can manipulate it in many ways 
ROne = Rockets(10)
for __ in range(1200):
  ROne.moveUp() # Rocket moved horizontal and vertically 1200 times
  
RTwo = Rockets(10)
for __ in range(1200):
  RTwo.moveUp() # Rocket moved horizontal and vertically 1200 times


print('-------------------')
print(RocketBoard.get_distance(ROne,RTwo))

