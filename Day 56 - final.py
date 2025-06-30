import csv, os

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    song = row["Song"]
    artists = row["Artist(s)"]
    dir = os.listdir()
    if artists not in dir:
      os.mkdir(artists)
    path = os.path.join(f"{artists}/", f"{song}")
    f = open(path, "w")
    f.close()