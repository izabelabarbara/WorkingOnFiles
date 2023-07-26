debugMode = False

import time, os

orders = [["NAME","TYPE","QUANTITY","SIZE","TOTAL"]]

try:
  f = open ("my.orders", "r")
  orders = eval(f.read())
  f.close()
except:
  print ("Unable to load file. Please check if a file \"my.orders\" exists")
  if debugMode:
    print (traceback)

pricePerSize = {"s":10, "m":15, "l":20}

def prettyPrinting():
  print()
  for row in orders:
    for i in row:
      print (f"{i:^15}|", end="")
    print ("\n")
    

def addingOrder():
  name = input("Please enter your name > ")
  taste = input("Please enter the type of pizza you are having > ")
  try:
    quantity = int(input("Please enter the quantity of the pizzas > ").strip())
  except:
    quantity = int(input("\033[33mInvalid value. \033[0mReenter the quantity. Make sure to put a whole number (like \"6\") > ").strip())
  size = input("Please choose the size (s/m/l) > ").strip()[0]
  total = f"$ {pricePerSize[size]*quantity}"
  row = [name, taste, quantity, size, total]
  orders.append(row)
  print ()
  time.sleep(1)
  print ("Great! I\'ve added the belo to your orders:")
  for heading in orders[0]:
    print (f"{heading:^15}|", end="")
  print ("\n")

  for i in row:
    print (f"{i:^15}|", end="")
  print ("\n")



def menu():
  os.system("clear")
  menu = input ("""Press 1 to add order
Press 2 to view all orders
> """)
  if menu == "1":
    addingOrder()
    time.sleep(2)
  elif menu == "2":
    prettyPrinting()
    time.sleep(4)



while True:
  menu()
  try:
    f = open ("my.orders", "w")
    f.write (str(orders))
    f.close()
  except:
    print("Unable to save file")
    if debugMode:
      print (traceback)
  
