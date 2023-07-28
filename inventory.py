debugMode = False
import os, time

# creating the inventory
inventory = []

#autoload any previous inventory
try:
  f = open("inventory.txt","r")
  inventory = eval(f.read())
  f.close()
except:
  print ("Unable to load file. Call help.")
  if debugMode:
    print (traceback)

# ADDING ITEMS
def add():
  os.system("clear")
  item = input ("What item do you want to add to your inventory > ").title()
  inventory.append(item)
  time.sleep(1)
  print()
  print(f"\033[32mI\'ve added {item} to your inventory.\033[0m")
  print()
  time.sleep(1)
  print ()
  next = input("Press enter if you would like to view menu again > ")
  while next == "":
    break

# VIEWING ITEMS
def view():
  os.system("clear")
  #counting items
  inventoryCounted = {"ITEM": "COUNT", "----------":"----------"}
  for i in inventory:
    if i not in inventoryCounted:
      j = inventory.count(i)
      inventoryCounted[i] = j
    else:
      continue
  
  # calculating column width GOES HERE:
  widthOptions = []
  for i in inventoryCounted:
    widthOptions.append(len(i))
  x = int(max(widthOptions)+4)
  
  # showing items 
  for i in inventoryCounted:
    print (f"\033[32m{i:^{x}}|{inventoryCounted[i]:^14}\033[0m")
  time.sleep(2)
  print ()
  next = input("Press enter if you would like to view menu again > ")
  while next == "":
    break
  
# REMOVING
def remove():
  os.system("clear")
  item = input("Which item do you want to remove? > ").title()
  #counting items
  if item not in inventory:
    print ()
    print (f"It looks like you don\'t have {item} in your inventory.")
    print ()
    time.sleep(1)
    print ("This is how your inventory looks like right now:")
    print()
    time.sleep(1)
    view()
  elif item in inventory:
    itemAmount = inventory.count(item)
    if itemAmount == 1:
      print()
      print (f"\033[32mYou have {itemAmount} {item} in your inventory.\033[0m")
      decision = input("Are you sure you want to remove it? (y/n) > ").strip().lower()[0]
      if decision == 'y':
        inventory.remove(item)
        print()
        time.sleep(1)
        print(f"\033[32mAll done! I\'ve removed {item} from your inventory.\033[0m")
        time.sleep(1)
        print ()
        next = input("Press enter if you would like to view menu again > ")
        while next == "":
          break
      else:
        print ()
        print ("\033[32mOk, we will keep it.\033[0m")
        time.sleep(1)
        print ()
        next = input("Press enter if you would like to view menu again > ")
        while next == "":
          break
    else:
      print (f"\033[32mYou have {itemAmount} {item}s in your inventory.\033[0m")
      x = int(input("How many do you want to remove? > "))
      for j in range (x):
        inventory.remove(item)
      time.sleep(1)
      print()
      print (f"All done! I\'ve removed {decision} {item}s from your inventory.")
      time.sleep(1)
      print ()
      next = input("Press enter if you would like to view menu again > ")
      while next == "":
          break

# MENU
def menu():
  os.system("clear")
  menu = input ("""Press 1 to add an item
Press 2 to view your inventory
Press 3 to remove an item
> """)
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    remove()

# STARTING THE PROGRAM (and autosave)
while True:
  menu()

  # autosave
  try:
    f = open ("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
  except:
    print ("Unable to save file. Please call your grandson.")
    if debugMode:
      print (traceback)
