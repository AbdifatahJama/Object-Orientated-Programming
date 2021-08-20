'''This module is the presentation module which is the interface that the user iteracts with. This interface can be developed into console based or a GUI'''

from architecture import *
import database1 as db
import locale as lc

lc.setlocale(lc.LC_ALL,'')

def intro():
  print('Welcome to the shopping cart program')

def command():
  print('\tCommands\nCart - Show the cart\nadd - add item into cart\ndel- Delete an item from the cart\nexit - Exit program')

command()

def get_product_row(product_row):
  '''Gets product based on its row'''
  return db.get_product_based_on_row(product_row)

def remove_item(cart):
  '''Removes item from cart. Method takes one argument which is the cart object itself'''
  if cart.itemCount()>0:
    print('This is your current cart')
    print(cart.list)
    item_number = int(input('Enter the product number in the list:'))
    cart.removeItem(item_number-1)
    print('Item deleted')
    print('Updated cart:',cart.__list)
  
  else:
    print('Cart is empty, cart must contain item(s) to remove an item')
    
def show_cart(cart):
  if cart.itemCount() == 0:
    print('Cart empty')
    
  else:
    print('Current list:',cart.list)
  
def checkout(cart):
  '''Checkout method'''
  pass

def main():
  buying = True
  i = 0 
  intro()
  command()
  cart = Cart()
  while buying:
    io = input('Command:')
    if io.lower() == 'add':
      i = 0
      product_row = int(input('item number:'))
      qauntity = int(input('Quantity:'))
      if product_row<= db.get_numbers_of_rows():
          print('\n')
          product_info = db.get_product(product_row)
          list = product_info[0]
          p = Products(list[0],list[1],list[2])
          lineitem = Lineitem(p,qauntity)
          cart.addItem(lineitem)
          print(list[0] + ' ' + 'added')
          
      else: 
        print('There is no' +' ' + 'row' + ' ' + str(product_row))  
                    
    
    elif io.lower() == 'del':
      i = 0
      remove_item(cart)
    
    elif io.lower() == 'cart':
      i = 0
      show_cart(cart)
      
    elif io.lower() == 'checkout':
      '''Checkouts all item within the cart list'''
      if len(cart.list)>=1:
        total = cart.final_total() # Iterates through each cart list which contains each product LineItem
        print('Final Price:',lc.currency(total,grouping=True))
        buying = False
      
      else:
        print('Your cart is empty')
    
    elif io.lower() == 'exit':
      print('Exiting..')
      buying = False
      
    else:
      '''If command not known user will be asked to enter valid command if user enters three wrong commands in a row they will be exited'''
      i+=1
      if i == 3:
        buying = False
        
  print('Exited')
  
main()
  
      
    
      
  
  

  
