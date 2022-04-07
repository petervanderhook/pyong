import pygame
from models import button

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
        self.buttons = pygame.sprite.Group()
        self.playduo = Button("./img/playclicked.png", "./img/play.png", 380, 400)
        self.playai = Button("./img/playclicked.png", "./img/play.png", 100, 400)
        self.plus = Button("./img/plusclicked.png", "./img/plus.png", 430, 140)
        self.minus = Button("./img/minusclicked.png", "./img/minus.png", 520, 140)
        self.buttons.add(self.playduo, self.playai, self.plus, self.minus)
        self.click_sound = pygame.mixer.Sound("./sounds/pop.wav")
        self.rounds = 3
        self.titlefont = pygame.font.Font('./spacemission.otf', 75)
        self.font = pygame.font.Font('./spacemission.otf', 35)
        self.toolfont = pygame.font.Font('./spacemission.otf', 15)
        self.title1 = self.titlefont.render("Total", True, (40, 86, 155))
        self.title2 = self.titlefont.render("Tennis", True, (40, 86, 155))
        self.tooltip = self.toolfont.render("Min: 3 \nMax: 10", True, ((125, 150, 245)))
        self.rounds_text = self.font.render(f"Rounds:   {self.rounds}", True, (125, 150, 245))
        self.ai_text = self.font.render("vs. AI", True, (40, 86, 155))
        self.player_text = self.font.render("vs. Player", True, (40, 86, 155))
        
        
    
    def process_loop(self):
        self.buttons.draw(self.window)
        
        #draw text
        self.rounds_text = self.font.render(f"Rounds:   {self.rounds}", True, (125, 150, 245))
        self.window.blit(self.title1, (50, 50))
        self.window.blit(self.title2, (160, 110))
        self.window.blit(self.rounds_text, (300, 200))
        self.window.blit(self.tooltip, (320, 230))
        self.window.blit(self.ai_text, (115, 450))
        self.window.blit(self.player_text, (360, 450))
    
    def process_event(self, event):
        pygame.event.pump()
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.check_mouse(mouse_pos):
                button.hover()
            else:
                button.unhover()
        if mouse_state[0]:
            if self.playduo.check_mouse(mouse_pos):
                print("Clicked duo")
                pass
            if self.playai.check_mouse(mouse_pos):
                print("Clicked ai")
                pass
            if self.plus.check_mouse(mouse_pos):
                print("Clicked plus")
                if self.rounds < 10:
                    self.rounds += 1
            if self.minus.check_mouse(mouse_pos):
                print("Clicked minus")
                if self.rounds > 3:
                    self.rounds -= 1

