import pygame
import sys


class Button(pygame.sprite.Sprite):

    def __init__(self, img_dir, x, y, color=pygame.Color("navy")):
        super().__init__()
        img = pygame.image.load(img_dir).convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        