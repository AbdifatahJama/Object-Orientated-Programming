import sqlite3
import csv
from architecture import Products,Lineitem,Cart

'''Database module'

Database stores the data of each Product object'''

def create_database():
  '''Creates database and table within it'''
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS Product(product_name TEXT,Price REAL, Discount Amount INTEGER)''')
  conn.commit()
  conn.close()

# create_database()
  
# def drop_table():
#   conn = sqlite3.connect('ProductDatabase.db')
#   c = conn.cursor()
#   c.execute('''DROP TABLE Product''')
#   conn.commit()
#   conn.close()

def add_row():
  conn = sqlite3.connect('ProductDatabase.db') # connects to database
  c = conn.cursor()
  c.execute('''INSERT INTO Product VALUES ("apple juice",10.5,5)''')
  conn.commit()
  conn.close()

# add_row()

def add_mutiple_rows():
  many = [('Lime Cake',7.50,10),('Basmati Rice',25,0),('Strawberries',3.80,0),('Light Bulbs(Pack of 10)',45,15),('Fridge',150,10),('Cupboard',50,4)]
  '''This method adds mutiple rows to the database table'''
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.executemany('''INSERT INTO Product VALUES(?,?,?)''',many)
  conn.commit()
  conn.close()
  
# add_mutiple_rows()
def delete_row():
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('''DELETE FROM Product WHERE rowid = 2''')
  conn.commit()
  conn.close()

# delete_row()
def get_product_based_on_row(row):
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('''SELECT * FROM Product WHERE rowid = ?''',(row,))
  product_data = c.fetchall()
  return product_data
def get_numbers_of_rows():
  '''Gets numbers of rows'''
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('''SELECT * FROM Product''')
  list = c.fetchall()
  return len(list)

def get_products_from_db():
  products_list = []
  '''Gets all product in database'''
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('''SELECT rowid,* FROM Product''') # Selects all rows in Product table 
  list = c.fetchall() # fetches all selected item
  for row in list:
    '''Iterates each row that cotains product information'''
    name = row[0]
    price = row[1]
    discountPercent = row[2]
    product = Products(name,price,discountPercent) # Instantiates product with attrubute name,price,discount
    products_list.append(product) # Adds each 
    
  return products_list

product = get_products_from_db()
first_product = product[1]

'''Line item takes product and the number of qauntities'''
lineitem = Lineitem(first_product,2)
cart = Cart() # Instiantaes cart object
cart.addItem(lineitem)
print(cart.getList())

def get_product(row):
  conn = sqlite3.connect('ProductDatabase.db')
  c = conn.cursor()
  c.execute('SELECT * FROM Product WHERE rowid = ?',(row,))
  list = c.fetchall()
  return list # Gets the one tuple of product information inside the list

a = get_product(1)
print(a[0][1])







  