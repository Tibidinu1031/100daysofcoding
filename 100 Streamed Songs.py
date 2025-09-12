import csv, os

print("Song Folders")
print("------------")
print()


count = 1

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    artist = row["Artist(s)"]
    allfiles = os.listdir()
    song = row["Song"]
    if artist not in allfiles:
      os.mkdir(artist)
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()
      

