from track import Track
import csv

with open ('database.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

tracks = []

for i in range(len(data)-2):
    name = data[i][0]
    retro = bool(data[i][1])
    rating = data[i][2]
    timesplayed = data[i][3]
    playedbase = data[i][4:]

    track = Track(name, retro, rating, timesplayed, playedbase)

    tracks.append(track)

week = data[len(data)-1][0]

tracks[0].name = 'Abandoned Boardwalk'

for track in tracks:
    print(track)
print()
print(week)