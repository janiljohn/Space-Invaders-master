import pygame as pg

class Home:

    def __init__(self, game):
        self.game= game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.initial_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)
        self.images = []
        self.prep_images()     


    def prep_images(self):
        self.prep_Letters("INVADERS", 90, color=(0,210,0), shift_y=160)
        self.prep_Letters("= 20 PTS", 40, shift_x=600, shift_y=350)
        self.prep_Letters("= 40 PTS", 40, shift_x=600, shift_y=400)
        self.prep_Letters("SPACE", 170, shift_y=40)        
        self.prep_Letters("= ???", 40, shift_x=610, shift_y=450)
        top_score = "High Score: " + str(self.game.scoreboard.high_score)
        self.prep_Letters("= 10 PTS", 40, shift_x=600, shift_y=300)
        self.prep_Letters(top_score, 40, shift_x=500, shift_y=700)

        icon1 = pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien_00.png'), 0, 3.5)
        self.images.append((icon1, (520, 290)))
        icon2 = pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__10.png'), 0, 3.5)
        self.images.append((icon2, (520, 330)))
        icon3 = pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__20.png'), 0, 3.5)
        self.images.append((icon3, (520, 380)))
        icon4 = pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/ufo.png'), 0, 3.2)
        self.images.append((icon4, (520, 450)))


        
        

    def prep_Letters(self, msg, size, color=(255,255,255), shift_x=0, shift_y=0):
        font = pg.font.SysFont(None, size)
        launch_img = font.render(msg, True, color, self.settings.bg_color)
        rect = launch_img.get_rect()
        if shift_y == 0:
            rect.centery = self.screen_rect.centery
        else:
            rect.top = shift_y
        if shift_x == 0:
            rect.centerx = self.screen_rect.centerx
        else:
            rect.left = shift_x

        self.images.append((launch_img,rect))

    def draw(self):
        for el in self.images:
            self.screen.blit(el[0], el[1])

    def reset(self):
        self.iamges = []
        self.prep_images()

