#from the jukebox_nested_data file, i import albums
from jukebox_nested_data import albums

#constants.
SONGS_LIST_INDEX = 3    
SONG_TITLE_INDEX = 1

#message pops up telling the user to choose one of the albums by putting in its matching number.
while True:
    print("Please choose your album:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

#if the user inputs an invalid the number such as 0, the programme will end.
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

#when the user has chosen the album they will be asked to pick a song from the album, again inputting their choices matching number.
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

#final message tells the user which song they are listening to.
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    
    #seperator 
    print("=" * 40)