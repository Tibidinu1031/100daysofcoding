import csv, os

print("Music Mania")
print()
artistList = []

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    if row["Artist(s)"] not in os.listdir():
      os.mkdir(row["Artist(s)"])

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  while True:
    for row in reader:
      song = row["Song"]
      fileExists = True
      try:
        f = open(f"{song}.txt", "r")
        f.write(eval(f.read()))
        f.close()
      except:
        fileExists = False
