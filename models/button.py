import pygame
import sys


class Button(pygame.sprite.Sprite):

    def __init__(self, click_dir, img_dir, x, y, color=pygame.Color("navy")):
        super().__init__()
        self.dir = img_dir
        self.img = pygame.image.load(self.dir).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        print(width, height)
        self.image = self.img
        clickedimg = pygame.image.load(click_dir).convert_alpha()
        self.clickedimg = clickedimg
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    

    def hover(self):
        self.image = self.clickedimg
    
    def unhover(self):
        self.image = self.img
    
    def check_mouse(self, pos_tuple):
        #Tuple of range of x covered by sprite rect
        mouse_x = pos_tuple[0]
        mouse_y = pos_tuple[1]
        x_range = (self.rect.topleft[0], self.rect.topleft[0] + self.img.get_width())
        y_range = (self.rect.topleft[1], self.rect.topleft[1] + self.img.get_height())
        if (mouse_x <= x_range[1]) and (mouse_x >= x_range[0]):
            if (mouse_y <= y_range[1]) and (mouse_y >= y_range[0]):
                return True
