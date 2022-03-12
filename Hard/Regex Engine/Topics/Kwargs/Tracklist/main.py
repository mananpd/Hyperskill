def tracklist(**kwargs):
    for artist, value in kwargs.items():
        print(artist)
        for album, song in value.items():
            print(f'ALBUM: {album} TRACK: {song}')
