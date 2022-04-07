import pygame
import sys


class Button(pygame.sprite.Sprite):

    def __init__(self, click_dir, img_dir, x, y, color=pygame.Color("navy")):
        """Basic class for buttons."""
        super().__init__()
        self.dir = img_dir
        self.img = pygame.image.load(self.dir).convert_alpha()
        self.image = self.img
        clickedimg = pygame.image.load(click_dir).convert_alpha()
        self.clickedimg = clickedimg
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = pygame.mixer.Sound('./sounds/click.wav')

    def hover(self):
        """Changes sprites image to hovered image"""
        self.image = self.clickedimg
    
    def unhover(self):
        """Changes sprites image to default image"""
        self.image = self.img
    
    def check_mouse(self, pos_tuple):
        """ Checks if the mouse position (pos_tuple) is within the bounds of a button's borders.
        If mouse within bounds, returns True."""
        #Tuple of range of x covered by sprite rect
        mouse_x = pos_tuple[0]
        mouse_y = pos_tuple[1]
        x_range = (self.rect.topleft[0], self.rect.topleft[0] + self.img.get_width())
        y_range = (self.rect.topleft[1], self.rect.topleft[1] + self.img.get_height())
        if (mouse_x <= x_range[1]) and (mouse_x >= x_range[0]):
            if (mouse_y <= y_range[1]) and (mouse_y >= y_range[0]):
                return True
            
    def click_sound(self):
        """Plays click sound when button is clicked."""
        pygame.mixer.Sound.play(self.click)
