class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment the song count and add the genre and artist
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Test cases
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
hotline_bling = Song("Hotline Bling", "Drake", "Rap")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
umbrella = Song("Umbrella", "Rihanna", "Pop")
folsom_prison_blues = Song("Folsom Prison Blues", "Johnny Cash", "Country")
friends_in_low_places = Song("Friends in Low Places", "Garth Brooks", "Country")
thunderstruck = Song("Thunderstruck", "AC/DC", "Rock")

print("Total Songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)
