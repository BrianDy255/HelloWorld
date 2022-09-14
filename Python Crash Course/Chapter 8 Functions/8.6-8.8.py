print("Exercise 8.6")
def city_country(city_name,country):
    """Outputs the city name and country for a function"""
    name_city_country = {"City Name": city_name.title(), "Country": country.title()}
    return name_city_country

place = city_country('santiago', 'chile')
print(place)

place = city_country('los angeles', 'USA')
print(place)

place = city_country('beijing', 'china')
print(place)

print("\nExercise 8.7")
def make_album(artist_name, album_title):
    """Provide a dictionary function for album name and title"""
    album = {"Artist": artist_name.title(), "Album Title": album_title.title()}
    return album

album_1 = make_album('metallica', 'ride the lightning')
print(album_1)

album_1 = make_album('linkin park', 'meteora')
print(album_1)

album_1 = make_album('michael jackson', 'bad')
print(album_1)

#adding optional parameter to exercise 8.7
def make_album(artist_name,album_title,track_list = None):
    album = {"Artist": artist_name.title(), "Album Title": album_title.title()}
    if track_list:
        album['Track List'] = track_list
    return album

album_1 = make_album('michael jackson', 'bad', track_list=32)
print(album_1)

print('\nExercise 8.8')
def make_album(artist_name,album_title):
    album = {"Artist Name": artist_name, "Album Title": album_title}
    return album

while True:
    ar_name = input("Input the artist name:>>> ")
    if ar_name == 'quit':
        break
    al_title = input("Input the album title:>>>")
    if al_title == 'quit':
        break
    full_album = make_album(ar_name.title(),al_title.title())
    print(full_album)

