def retrieve_songs_by_mood(songs, mood):
    return [song for song in songs if song["mood"].lower() == mood.lower()]
