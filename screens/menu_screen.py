import pygame

from models.button import Button
from .base_screen import Screen
from constants import LIMITS

class MenuScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Create objects
        #self.ball = Ball()
        #self.ball.launch()
        pygame.mixer.music.load("./sounds/music.wav")
        pygame.mixer.music.play(-1)

        self.play = Button("./img/play.png", 130, 40)
        self.plus = Button("./img/plus.png", 45, 40)
        pygame.draw(self.plus, 50, 50)
        self.click_sound = pygame.mixer.Sound("./sounds/pop.wav")
    
    def process_loop(self):
        pass
    
    def process_event(self, event):
        pass
