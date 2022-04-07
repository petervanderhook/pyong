import pygame
from models import Button, Background
from .base_screen import Screen
from constants import LIMITS

class MenuScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        """Constructor for menu screen."""
        super().__init__(*args, **kwargs)

        #Values to be accessed/returned
        self.rounds = 3
        self.close = False
        self.gamestate = None
        self.practice = False
        
        # Loads and plays music, sets name of window and sounds
        pygame.mixer.music.load("./sounds/music.wav")
        pygame.mixer.music.play(-1)
        pygame.display.set_caption('Total Tennis')
        self.click_sound = pygame.mixer.Sound("./sounds/pop.wav")

        # Makes buttons and adds them to a group
        self.buttons = pygame.sprite.Group()
        self.playduo = Button("./img/playclicked.png", "./img/play.png", 380, 500)
        self.playai = Button("./img/playclicked.png", "./img/play.png", 100, 500)
        self.playpractice = Button("./img/practiceclicked.png", "./img/practice.png", 100, 360)
        self.plus = Button("./img/plusclicked.png", "./img/plus.png", 520, 140)
        self.minus = Button("./img/minusclicked.png", "./img/minus.png", 430, 140)
        self.buttons.add(self.playduo, self.playai, self.plus, self.minus, self.playpractice)

        # Fonts
        self.titlefont = pygame.font.Font('./spacemission.otf', 75)
        self.font = pygame.font.Font('./spacemission.otf', 35)
        self.toolfont = pygame.font.Font('./spacemission.otf', 15)
        self.title1 = self.titlefont.render("Total", True, (40, 86, 155))
        self.title2 = self.titlefont.render("Tennis", True, (40, 86, 155))  
        self.tooltip = self.toolfont.render("Min: 3 \nMax: 10", True, ((125, 150, 245)))
        self.rounds_text = self.font.render(f"Rounds:   {self.rounds}", True, (125, 150, 245))
        self.ai_text = self.font.render("vs. AI", True, (40, 86, 155))
        self.practice_text = self.font.render("Practice Mode", True, (40, 86, 155))
        self.player_text = self.font.render("vs. Player", True, (40, 86, 155))

        # Background image
        self.background = Background('./img/background.png')
        self.images = pygame.sprite.Group()
        self.images.add(self.background)

        
    
    def process_loop(self):
        """Draws background, buttons, and text in the menu screen window. If ESC is pressed, quits the game.
        """
        # draw buttons and images
        self.images.draw(self.window)
        self.buttons.draw(self.window)
        # draw text
        self.rounds_text = self.font.render(f"Rounds:   {self.rounds}", True, (125, 150, 245))
        self.window.blit(self.title1, (50, 50))
        self.window.blit(self.title2, (160, 110))
        self.window.blit(self.rounds_text, (300, 200))
        self.window.blit(self.tooltip, (320, 230))
        self.window.blit(self.ai_text, (115, 450))
        self.window.blit(self.practice_text, (35, 310))
        self.window.blit(self.player_text, (360, 450))
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.playai.click_sound()
            print("End game via escape")
            self.running=False
    
    def process_event(self, event):
        """Updates button colors if the mouse hovers them, 
        and checks where the mouse is located when it clicks, to know if a button is pressed."""
        pygame.event.pump()
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.check_mouse(mouse_pos):
                button.hover()
            else:
                button.unhover()
        if mouse_state[0]:
            if self.playpractice.check_mouse(mouse_pos):
                print("Clicked practice")
                self.playpractice.click_sound()
                self.gamestate = [1000, True]
                self.running = False
                return self.gamestate
            if self.playduo.check_mouse(mouse_pos):
                print("Clicked duo")
                self.playduo.click_sound()
                self.gamestate = [self.rounds, False]
                self.running = False
                return self.gamestate
            if self.playai.check_mouse(mouse_pos):
                self.playai.click_sound()
                print("Clicked ai")
                self.gamestate = [self.rounds, True]
                self.running = False
                return self.gamestate
            if self.plus.check_mouse(mouse_pos):
                self.plus.click_sound()
                print("Clicked plus")
                if self.rounds < 10:
                    self.rounds += 1
            if self.minus.check_mouse(mouse_pos):
                self.minus.click_sound()
                print("Clicked minus")
                if self.rounds > 3:
                    self.rounds -= 1

