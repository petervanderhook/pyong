import pygame
from constants import LIMITS
import time
import random

class Paddle(pygame.sprite.Sprite):
    """Paddle class"""

    def __init__(self, position, color=None):
        """Constructor for paddle"""
        super().__init__()

        # Default size
        self.size = (10, 100)

        # Default speed
        self.speed = 10

        # Defaul score
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
    
    def check_move(self, ball_y, ball_offlimits=False):
        """ Class that checks if the paddle needs to move up or down.
        Used by the ai class"""
        
        # Checks if the ball is offlimits. Wont move if the ball is out of bounds
        if ball_offlimits != True:
            # Sets speed to 5 (or its too strong!!)
            self.speed = 5
            # Variation, (height is 100px, so the detection range of the paddle is +- 25 pixels on each edge of the paddle)
            vary = random.randrange(-125, 25)
            # ball.rect.y has vary added to it
            ball_y += vary
            width = self.image.get_width()
            core = self.rect.y + (width)
            # Checks if the center of the paddle is above or below the ball's y coords +- the variation and moves accordingly
            if core > ball_y:
                self.up()
            elif core < ball_y:
                self.down()
            else:
                pass

