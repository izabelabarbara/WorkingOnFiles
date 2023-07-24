import os, time 

while True:
  f = open("high.score", "a+")
  os.system("clear")
  initials = input ("INITIALS > ").strip().upper()
  score = input ("SCORE > ").strip()
  f.write(f"{initials} {score}\n")
  f.close()
  print()
  print ("ADDED!")
  time.sleep(0.6)