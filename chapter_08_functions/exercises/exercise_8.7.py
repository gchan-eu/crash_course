def make_album(artist_name, album_title, number_of_tracks=0):
    album = {'name': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album

album = make_album('jim morisson', 'light my fire', 10)
print(album)
album = make_album(artist_name='madonna', album_title='sex and the city', number_of_tracks=12)
print(album)
album = make_album(artist_name='ac/dc', album_title='thunderstrike')
print(album)
