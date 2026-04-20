import pygame
import os



class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base_path = os.path.dirname(__file__)
        music_path = os.path.join(base_path, "music")

        self.playlist = [
            os.path.join(music_path, f)
            for f in os.listdir(music_path)
            if f.endswith(".wav")
        ]

        self.current = 0
        self.playing = False

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current])
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play()

    def previous(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        if self.playlist:
            return os.path.basename(self.playlist[self.current])
        return "No track"
    
    