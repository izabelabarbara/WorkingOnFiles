import os, csv

# create a directory "Artists" to put folders inside
if "Artists" not in os.listdir():
  os.mkdir("Artists")

with open("100MostStreamedSongs.csv") as file:
  data = csv.DictReader(file)
  for row in data:
    # create a folder
    folderName = str(row["Artist(s)"])
    pathName = f"Artists/{folderName}"
    if not os.path.exists(pathName):
      os.mkdir(pathName)
      
    # add a song (as a blank file) to a folder
    songName = str(row["Song"])
    songPathName = f"Artists/{folderName}/{songName}.txt"
    if not os.path.exists(songPathName):
      file = os.path.join(f"Artists/{folderName}/",f"{songName}.txt")
      f = open(file, "w")
      f.write("")
      f.close()
