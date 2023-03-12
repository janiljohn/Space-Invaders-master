import pygame as pg
from ship import Ship
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = game.score_data['high_score']
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.game = game

        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 36)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()

    def increment_score(self, alien_type, point=0): 
        if alien_type == 0:
            score_inc = self.settings.pink_alien
        elif alien_type == 1:
            score_inc = self.settings.blue_alien
        elif alien_type == 2:
            score_inc = self.settings.green_alien
        else:
            score_inc = point
        self.score += score_inc
        self.update_score()
        self.prep_high_score()
        self.prep_score()

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.game.score_data['high_score'] = self.high_score

    def prep_score(self): 
        score_str = "Score: " + str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        self.ships = []
        for ship_number in range(self.game.ship.ships_left):
            ship = Ship(self.game)
            ship.rect.centerx = 35 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.append(ship)


    def prep_level(self): 
        level_str = "Level: " + str(self.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 50

    def prep_high_score(self): 
        hs_str = "Top Scores: " + str(self.high_score)
        self.hs_image = self.font.render(hs_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = 20


    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()
        

    def draw(self):
        if self.stats.game_active:
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.level_image, self.level_rect)
            self.screen.blit(self.hs_image, self.hs_rect)
            for ship in self.ships:
                ship.draw()
