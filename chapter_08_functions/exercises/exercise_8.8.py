def make_album(artist_name, album_title, number_of_tracks=0):
    album = {'name': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album

while True:
    print("\nEnter 'q' to quit.")
    album_artist = input("Enter album artist: ")
    if album_artist == 'q':
        break
    album_title = input("Enter album title: ")
    if album_title == 'q':
         break
    album = make_album(artist_name=album_artist, album_title=album_title)
    print(album)