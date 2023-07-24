import random, time, os

def add():
  f = open("my.ideas", "a+")
  addIdea = input ("IDEA > ")
  f.write(f"{addIdea}\n")
  f.close()

def show():
  f = open("my.ideas", "r")
  ideas = []
  while True:
    idea = f.readline()
    if idea == '':
      break
    ideas.append(idea)
  chosenIdea = random.choice(ideas)
  print (chosenIdea)
  f.close()

while True:
  menu = input ("Press 1 to add idea, press 2 to show random idea > ")
  if menu == "1":
    add()
  elif menu == "2":
    show()
  time.sleep(1)
  os.system("clear")
