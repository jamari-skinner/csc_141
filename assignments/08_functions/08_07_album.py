def make_album(artist, title):
    """Return a dictionary containing album information."""
    album = {'artist': artist.title(), 'title': title.title()}
    return album

album1 = make_album('drake', 'views')
album2 = make_album('kendrick lamar', 'damn')
album3 = make_album('kaash paige', 'teenage fever')

print(album1)
print(album2)
print(album3)