import pygame as pg
from laser import LaserType
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        ufo_sound = pg.mixer.Sound('spaceInvaders_start/sounds/oscillating.wav')
        pg.mixer.music.set_volume(0.1)
        self.bg_music = bg_music
        alienlaser_sound = pg.mixer.Sound('spaceInvaders_start/sounds/alienlaser.wav')
        photontorpedo_sound = pg.mixer.Sound('spaceInvaders_start/sounds/photon_torpedo.wav')
        gameover_sound = pg.mixer.Sound('spaceInvaders_start/sounds/gameover.wav')
        self.sounds = {'alienlaser': alienlaser_sound, 'photontorpedo': photontorpedo_sound, 'oscillating': ufo_sound,
                       'gameover': gameover_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type): 
        pg.mixer.Sound.play(self.sounds['alienlaser' if type == LaserType.ALIEN else 'photontorpedo'])
    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('spaceInvaders_start/sounds/gameover.wav')
        self.play_bg()
        time.sleep(2.8)

    def reset(self):
        pg.mixer.music.stop()
        pg.mixer.music.load(self.bg_music)
        self.play_bg()

    def ufo(self):
        pg.mixer.Sound.play(self.sounds['oscillating'])
