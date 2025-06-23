def make_album(artist, title, number_of_songs=None):
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

print("Enter album details (type 'quit' at any time to stop):")

while True:
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    songs = input("Number of songs (optional): ")
    if songs.lower() == 'quit':
        break
    songs = int(songs) if songs else None

    album = make_album(artist, title, songs)
    print(f"\nAlbum created: {album}\n")