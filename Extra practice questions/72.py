# Modified function with optional number_of_songs parameter
def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

# Calls with and without song count
album1 = make_album('arijit singh', 'soulful hits')
album2 = make_album('atif aslam', 'romantic vibes', 10)
album3 = make_album('ar rahman', 'musical magic', 8)

# Print albums
print(album1)
print(album2)
print(album3)