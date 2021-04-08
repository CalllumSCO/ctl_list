from track import Track
import csv

with open ('database.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

tracks = []

for i in range(len(data)-2):
    name = data[i][0]
    if int(data[i][1]) == 1:
        retro = True
    else:
        retro = False
    rating = int(data[i][2])
    timesplayed = int(data[i][3])
    playedbase = data[i][4:]

    for i in range (len(playedbase)):
        playedbase[i] = int(playedbase[i])
    track = Track(name, retro, rating, timesplayed, playedbase)

    tracks.append(track)

week = data[len(data)-1][0]
tracks[0].name = 'Abandoned Boardwalk'

oneRating = []
twoRating = []
threeRating = []
fourRating = []
fiveRating = []
retros = []

for track in tracks:
    if track.retro:
        retros.append(track)
    
    if track.rating == 1:
        oneRating.append(track)
    elif track.rating == 2:
        twoRating.append(track)
    elif track.rating == 3:
        threeRating.append(track)
    elif track.rating == 4:
        fourRating.append(track)
    else:
        fiveRating.append(track)

for track in retros:
    print(track)