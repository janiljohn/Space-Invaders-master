import pygame.font
class Home():
    def __init__(self, screen, msg, height_factor, scale):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200/scale, 50/scale
        self.button_color = (0, 255, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.screen.get_width()/2,self.screen.get_height()/height_factor)

        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.height, self.msg_image_rect.width = 200/scale, 50/scale
        self.msg_image_rect.center = (self.screen.get_width()/2,self.screen.get_height()/height_factor)

        # The button message needs to be prepped only once.
        # self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # self.msg_image = self.font.render(msg, True, self.text_color,
        # self.button_color)
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.rect.width, self.rect.height)

    def draw_button(self):
        # Draw blank button and then draw message.
        # self.screen.fill(self.button_color, self.rect)
        # self.screen.fill(self.text_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)