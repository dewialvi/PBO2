class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
        print("Title :", song.title)

class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        print("Play Music")
        
song1 = Song("Lose Yourself", "Eminem")
song2 = Song("Someone Like You", "Adele")
playlist = Playlist()
media_player = MediaPlayer(playlist)
print("."*20)
playlist.add_song(song1)
playlist.add_song(song2)
media_player.playlist.songs # output: [song1, song2]
