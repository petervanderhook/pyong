import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self, image_dir):
        super().__init__()

        img = pygame.image.load(image_dir).convert_alpha()

        self.image = img
        self.rect = self.image.get_rect()
