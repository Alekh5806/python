# Function to build album dictionary
def make_album(artist, title):
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    return album

# Function calls
album1 = make_album('arijit singh', 'soulful hits')
album2 = make_album('atif aslam', 'romantic vibes')
album3 = make_album('ar rahman', 'musical magic')

# Print album details
print(album1)
print(album2)
print(album3)