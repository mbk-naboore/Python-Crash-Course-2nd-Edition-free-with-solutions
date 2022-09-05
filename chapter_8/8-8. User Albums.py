def make_album(artist_name, album_title, number=None):
    dictionary = {"artist name": artist_name.title(), "album name": album_title.title()}
    if number:
        dictionary["number of songs"] = number
    return dictionary


while True:
    print("\nPlease give us information about an album.")
    print("If you're done, type 'quit' to exit.")

    artist = input("Please name the artist: ")
    if artist == "quit":
        break
    title = input("Please name the title of the album: ")
    if title == "quit":
        break

    print(make_album(artist, title))
