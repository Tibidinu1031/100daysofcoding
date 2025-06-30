import csv, os

with open("100MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Artist(s)"])