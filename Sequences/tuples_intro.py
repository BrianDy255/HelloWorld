albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Ligthening", "Metallica", 1984)]

for name, artist, year in albums:
    print(f'Artist:{name}, Artist: {artist}, Year: {year}')

for album in albums:
    name, artist, year = album
    print(f'Artist:{name}, Artist: {artist}, Year: {year}')