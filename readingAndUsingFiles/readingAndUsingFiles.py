import time, os

f = open ("high.score","r")

scoresAndUsers = {}
scores = []

while True:
  lineList = f.readline().split()
  if lineList == []:
    break
  scores.append(int(lineList[1]))
  scoresAndUsers[lineList[1]] = lineList[0]

f.close()

winnerPoints = str(max(scores))


print ("🌟 Current Leader 🌟")
print ()
time.sleep(0.3)
print ("Analyzin high scores .")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ..")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ...")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ....")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores .....")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores .")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ..")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ...")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ....")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores .....")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores .")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ..")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ...")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores ....")
time.sleep (0.3)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
print ("Analyzin high scores .....")
time.sleep (0.5)
os.system("clear")
print ("🌟 Current Leader 🌟")
print ()
time.sleep(1)
print (f"Current leader is {scoresAndUsers[winnerPoints]} with {winnerPoints} points!!!")

