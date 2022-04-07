import pygame


class Background(pygame.sprite.Sprite):
    """ Basic class for background images."""

    def __init__(self, image_dir):
        """Constructor for background"""
        super().__init__()

        img = pygame.image.load(image_dir).convert_alpha()

        self.image = img
        self.rect = self.image.get_rect()
