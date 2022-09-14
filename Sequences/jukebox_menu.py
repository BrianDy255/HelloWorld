from nested_data import albums

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1
while True:
    print("Please choose your album (Invalid choice exits)")
    for index, (title,artist, year, songs) in enumerate(albums):
        print(f'{index + 1} {title}')

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]
    else:
        continue

    print("Please Choose your Song:")
    for index, (track_number, songs) in enumerate(songs_list):
        print(f'Track Number: {index + 1}, "Song: {songs}')

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONGS_TITLE_INDEX]
    else:
        continue

    print(f"Now Playing:\n \t {title}")
    print(("***" * 50), '\n')