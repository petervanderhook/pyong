import pygame
from constants import LIMITS
import time
import random

class Paddle(pygame.sprite.Sprite):
    """Paddle class"""

    def __init__(self, position, color=None):
        super().__init__()

        # Default size
        self.size = (10, 100)
        self.score = 0

        # Default speed
        self.speed = 10
        self.score = 0

        if not color:
            color = (0, 0, 0)
        self.refresh_rect(color)

        # Starting positions
        if position == "left":
            self.rect.x = LIMITS["left"] + 10
        elif position == "right":
            self.rect.x = LIMITS["right"] - self.size[0] - 10

        self.rect.y = LIMITS["down"] // 2

    def refresh_rect(self, color):
        """Updates the sprite / rect based on self.size"""
        self.image = pygame.Surface(self.size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def up(self):
        """Move the paddle up"""
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < LIMITS["up"]:
            self.rect.y = LIMITS["up"]

    def down(self):
        """Move the paddle down"""
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > LIMITS["down"] - self.size[1]:
            self.rect.y = LIMITS["down"] - self.size[1]
    
    def check_move(self, ball_y):
        self.speed = 5
        vary = random.randrange(-25, 40)
        ball_y += vary
        width = self.image.get_width()
        core = self.rect.y + (width)
        if core > ball_y:
            self.up()
        elif core < ball_y:
            self.down()
        else:
            pass

