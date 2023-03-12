from ast import Or
from email.headerregistry import HeaderRegistry
from random import randint
import pygame as pg
from pygame.sprite import Sprite, Group
from laser import Lasers
from timer import Timer

class Ufo(Sprite):


    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.game = game
        self.settings = game.settings
        self.direction = 1
        self.image = pg.image.load('spaceInvaders_start/images-1/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.sb = game.scoreboard
        self.dying = self.dead = False
        self.val = randint(10, 21) * 10
        self.text_color = (255, 255, 255)
        self.start = True
        self.font = pg.font.SysFont(None, 48)
        self.prep_val()
        self.ufo_images = [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/ufo.png'), 0, 2),
                           ]
        self.ufo_explosion_images = [self.score_image, self.score_image, pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images/explosion_blank.png'), 0, 1.5)]

        self.timer_normal = Timer(self.ufo_images, 0, delay=300)
        self.timer_explosion = Timer(self.ufo_explosion_images, delay=500, is_loop=False)
        self.timer = self.timer_normal 

    def prep_val(self):
        rounded_score = self.val
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.rect
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20

    def check_edges(self): 
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    def hit(self):
        if not self.dying:
            self.dying = True
            self.timer = self.timer_explosion
            self.sb.increment_score(3, self.val)

    def update(self): 
        if self.timer == self.timer_explosion and self.timer.is_expired():
            self.dead = True
            self.kill()
        settings = self.settings
        self.x += (settings.ufo_speed * self.direction)
        self.rect.x = self.x
        self.draw()
    def draw(self): 
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery + 30
        self.screen.blit(image, rect)

class Alien(Sprite): 
    # alien_images = [[pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien_03-{n}.png'), 0, 3.7) for n in range(2)],
    #                 [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__1{n}.png'), 0, 3.7) for n in range(2)],
    #                 [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__2{n}.png'), 0, 3.7) for n in range(2)]]

    alien_images = [[pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien_0{n}.png'), 0, 3.7) for n in range(2)],
                    [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__1{n}.png'), 0, 3.7) for n in range(2)],
                    [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/alien__2{n}.png'), 0, 3.7) for n in range(2)],
                    [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/UFO.png'), 0, 3.7) for n in range(1)]]

    aelist0 = ['1','2', '3', 10, 10, 'blank']
    aelist1 = ['1','2', '3', 20, 20, 'blank']
    aelist2 = ['1','2', '3', 30, 30, 'blank']
    alien_explosion_images = [[pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/explosion_{el}.png'), 0, 1.5) for el in aelist2],
                              [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/explosion_{el}.png'), 0, 1.5) for el in aelist1] ,
                              [pg.transform.rotozoom(pg.image.load(f'spaceInvaders_start/images-1/explosion_{el}.png'), 0, 1.5) for el in aelist0]]
 

    def __init__(self, game, type, alien_number):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('spaceInvaders_start/images/alien0.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.type = type
        self.sb = game.scoreboard
        self.dying = self.dead = False
        
        start_index = 0 if alien_number % 2 == 0 else 1
        self.timer_normal = Timer(Alien.alien_images[type], start_index=start_index, delay=300)
        self.timer_explosion = Timer(Alien.alien_explosion_images[type], delay=300, is_loop=False)
        self.timer = self.timer_normal                                    

    def check_edges(self): 
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    def check_bottom_or_ship(self, ship):
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom or self.rect.colliderect(ship.rect)
    def hit(self):
        if not self.dying:
            self.dying = True
            self.timer = self.timer_explosion
            self.sb.increment_score(self.type)
    def update(self): 
        if self.timer == self.timer_explosion and self.timer.is_expired():
            self.kill()
        settings = self.settings
        self.x += (settings.alien_speed * settings.fleet_direction)
        self.rect.x = self.x
        self.draw()
    def draw(self): 
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery
        self.screen.blit(image, rect)


class Aliens:
    def __init__(self, game): 
        self.model_alien = Alien(game=game, type=0, alien_number=0)
        self.game = game
        self.sb = game.scoreboard
        self.aliens = Group()
        self.ufo = Ufo(game=self.game)
        self.alien_tier = 0
        
        self.ufo_alive = True

        self.ship_lasers = game.ship_lasers.lasers    # a laser Group
        self.aliens_lasers = game.alien_lasers

        self.screen = game.screen
        self.settings = game.settings
        self.shoot_requests = 0
        self.ship = game.ship
        self.create_fleet()

    def get_number_aliens_x(self, alien_width):
        available_space_x = self.settings.screen_width - 6 * alien_width
        number_aliens_x = int(available_space_x / (1.2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, ship_height, alien_height):
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (1 * alien_height))
        number_rows = 6
        return number_rows        

    def reset(self):
        # pass
        self.aliens.empty()
        self.create_fleet()
        self.aliens_lasers.reset()
        self.alien_tier = 0

    def create_alien(self, alien_number, row_number):
        type = row_number // 2
        alien = Alien(game=self.game, type=type, alien_number=alien_number)

        # alien = Alien(game=self.game, type=0)
        alien_width = alien.rect.width

        alien.x = alien_width + 1.5 * alien_width * alien_number 
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * row_number + 80
        self.aliens.add(alien)     

    def create_fleet(self):
        number_aliens_x = self.get_number_aliens_x(self.model_alien.rect.width) 
        number_rows = self.get_number_rows(self.ship.rect.height, self.model_alien.rect.height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                   self.create_alien(alien_number, row_number)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites(): 
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def check_fleet_bottom(self):
        for alien in self.aliens.sprites():
            if alien.check_bottom_or_ship(self.ship):
                self.ship.hit()
                break

    def check_fleet_empty(self):
        if len(self.aliens.sprites()) == 0:
            print('Aliens all gone!')
            self.game.reset()

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def shoot_from_random_alien(self):
        self.shoot_requests += 1
        if self.shoot_requests % self.settings.aliens_shoot_every != 0:
            return
    
        num_aliens = len(self.aliens.sprites())
        alien_num = randint(0, num_aliens)
        i = 0
        for alien in self.aliens.sprites():
            if i == alien_num:
                self.aliens_lasers.shoot(game=self.game, x=alien.rect.centerx, y=alien.rect.bottom)
            i += 1


    def check_collisions(self):  
        collisions = pg.sprite.groupcollide(self.aliens, self.ship_lasers, False, True)  
        if collisions:
            if self.alien_tier == 0 and len(self.aliens) < 44:
                pg.mixer.music.stop()
                pg.mixer.music.load('spaceInvaders_start/sounds/startrek_2.wav')
                pg.mixer.music.play(-1, 0.0)
                self.alien_tier = 1
            elif self.alien_tier == 1 and len(self.aliens) < 22:
                pg.mixer.music.stop()
                pg.mixer.music.load('spaceInvaders_start/sounds/startrek_3.wav')
                pg.mixer.music.play(-1, 0.0)
                self.alien_tier = 2
            for alien in collisions:
                alien.hit()

        collisions = pg.sprite.groupcollide([self.ufo], self.ship_lasers, False, True)  
        if collisions:
            self.ufo.hit()
            self.ufo_death = pg.time.get_ticks()
            self.ufo_reset = randint(1000,1501) * 10

    def reset_ufo():
        pass

    def ufo_update(self):
        if not self.ufo.dead:
            if self.ufo.check_edges():
                self.ufo.direction *= -1
            self.ufo.update()
        elif pg.time.get_ticks() - self.ufo_death > self.ufo_reset:
            self.ufo = Ufo(self.game)

    def update(self): 
        self.check_fleet_edges()
        self.check_fleet_bottom()
        self.check_collisions()
        self.check_fleet_empty()
        self.shoot_from_random_alien()
        self.ufo_update()
        for alien in self.aliens.sprites():
            if alien.dead:      # set True once the explosion animation has completed
                alien.remove()
            alien.update()
        self.aliens_lasers.update()

    # def draw(self): 
    #     for alien in self.aliens.sprites(): 
    #         alien.draw() 
