def make_album(artist, title):
    """Return a dictionary containing album information."""
    album = {'artist': artist.title(), 'title': title.title()}
    return album

while True:
    print("\nEnter album information (or 'quit' to stop):")

    artist = input("Artist name: ")
    if artist == 'quit':
        break

    title = input("Album title: ")
    if title == 'quit':
        break

    album = make_album(artist, title)
    print(album)