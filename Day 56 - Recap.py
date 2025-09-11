import csv, os

print("Song Folders")
print("------------")
print()

allfiles = os.listdir()
count = 1

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    artist = row["Artist(s)"]
    song = row["Song"]
    if artist not in allfiles:
      os.mkdir(artist)
      for row in reader:  
        song = f"{row['Song']}.mp3"
        os.popen(f"cp {song} {artist}/{song}")
      
print()
for item in allfiles:
  print(item)
