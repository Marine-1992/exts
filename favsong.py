fav_song = ["Hello", "S.O.S", "Feeling Good", "Isn't she lovely"]
fav_song.sort()
print(fav_song)
print(fav_song[0])
print(fav_song[1])
print(fav_song[2])
print(fav_song[3])
fav_song.append("Paint it black")
number_of_songs = len(fav_song)
message = "There are " + str(number_of_songs) + " songs in the array."
print(message)
fav_song.pop(2)
print(fav_song)
print(len(fav_song))


