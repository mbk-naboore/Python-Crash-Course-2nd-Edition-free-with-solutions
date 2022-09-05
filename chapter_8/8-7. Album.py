def make_album(artist_name, album_title, number=None):

    dictionary = {"artist name": artist_name.title(), "album name": album_title.title()}
    if number:
        dictionary["number of songs"] = number
    return dictionary


art1 = make_album("Muhammad Ali", "Test1_album")
print(art1)


print(make_album("mike tyson", "Test2_album"))


art3 = make_album(artist_name="mbk-naboore", album_title="Test3_album", number=15)
print(art3)
