import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x150")

        self.playlist = []
        self.current_track = 0

        pygame.mixer.init()

        self.create_ui()
    
    def create_ui(self):
        # Create buttons
        play_button = tk.Button(self.root, text="Play", command=self.play_music)
        pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        next_button = tk.Button(self.root, text="Next", command=self.next_track)
        prev_button = tk.Button(self.root, text="Previous", command=self.prev_track)
        add_button = tk.Button(self.root, text="Add Music", command=self.add_music)

        play_button.pack()
        pause_button.pack()
        stop_button.pack()
        next_button.pack()
        prev_button.pack()
        add_button.pack()
    
    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
    
    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()

    def prev_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
