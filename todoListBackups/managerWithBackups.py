from tabulate import tabulate
import os, time

manager = [["TASK", "DEADLINE", "PRIORITY"]]

files = os.listdir()
if "todolist.txt" not in files: 
  f = open("todolist.txt", "w")
  f.write(str(manager))
  f.close()

f = open ("todolist.txt","r+")
manager = eval(str(f.read()))
f.close()

def quittingOrMenu():
  print ()
  next = input ('''Press \'q\' if you would like to quit.
Press enter if you would like to view menu.
> ''')
  if next == 'q':
    exit()

def addToManager():
  print ()
  task = input("Task > ").title()
  deadline = input("Deadline > ").capitalize()
  priority = input("Priority (high/medium/low) > ").strip().upper()
  row = [task, deadline, priority]
  manager.append(row)
  time.sleep(0.5)
  print ()
  print (f"Sure, I have added {task} to your list.")
  time.sleep(2)
  quittingOrMenu()

def deleteFromManager():
  showTheManager()
  itemToDelete = input ("What do you want to delete > ")
  for row in manager:
    if itemToDelete in row:
      manager.remove(row)
      print ()
      time.sleep(0.5)
      print (f"Sure, I have deleted {itemToDelete} from your list.")
      time.sleep(2)
      quittingOrMenu()

def viewingTheManager():
  print ()
  print(tabulate(manager, colalign=('center', 'center', 'center'),tablefmt='fancy_grid'))
  time.sleep(4)
  quittingOrMenu()

def showTheManager():
  print ()
  print ("This is your list now:")
  print(tabulate(manager, colalign=('center', 'center', 'center'),tablefmt='fancy_grid'))
  time.sleep(1)
  
def viewingByPriority():
  priorityManager = []
  print ()
  priorityChosen = input("Would you prefer to view tasks with high, medium or low priority? > ").upper()
  for row in manager:
    if priorityChosen in row:
      priorityManager.append(row)
  print ()
  time.sleep(0.5)
  print(tabulate(priorityManager, colalign=('center', 'center', 'center'),tablefmt='fancy_grid'))
  time.sleep(2)
  quittingOrMenu()

def viewingOptions():
  print ()
  option = input("Would you like to view all the items or view by priority? > ").lower()
  if 'p' in option:
    viewingByPriority()
  else:
    viewingTheManager()

def editingManager():
  showTheManager()
  taskChoice = input("Which task would you like to edit? > ").title()
  editedRow = []
  for row in manager:
    if taskChoice in row:
      i = manager.index(row)
      itemChoice = input("Which item would you like to edit? (task/deadline/priority) > ").strip()[0]
      if itemChoice == 't':
        j=0
      elif itemChoice == 'd':
        j=1
      elif itemChoice == 'p':
        j=2
      manager[i][j] = input (f'What would you like to change {manager[i][j]} to? > ')
      editedRow.append(manager[i])
      print ()
      print ("Cool! This is how it looks now:")
      print(tabulate(editedRow, colalign=('center', 'center', 'center'),tablefmt='fancy_grid'))
      time.sleep(2)

def menu():
  os.system("clear")
  print ("🌟 Life Organizer 🌟")
  print ()
  time.sleep(0.5)
  action = input("Would you like to add, remove, view or edit what\'s on your TODO list? > ").strip().lower()[0]
  if action == 'a':
    addToManager()
  elif action == 'r':
    deleteFromManager()
  elif action == 'v':
    viewingOptions()
  elif action == 'e':
    editingManager()
    
while True:
  menu()
  backupNumber = 0 
  if "Backup" not in files:
    os.mkdir("Backup")
  backupFile = os.path.join("Backup/",f"backup{backupNumber}.txt")
  g = open(backupFile, "w")
  g.write(str(manager))
  g.close()

  f = open("todolist.txt", "w")
  f.write (str(manager))
  f.close()

  backupNumber += 1
