import pygame
from models import Background, Button
from .base_screen import Screen
from constants import LIMITS, WINDOW_HEIGHT as winy, WINDOW_WIDTH as winx


class EndScreen(Screen):

    def __init__(self, *args, **kwargs):
        """Constructor for the end screen"""
        super().__init__(*args, **kwargs)
        pygame.init()

        # Variables
        self.text = "error"

        # Load images and buttons
        self.background = Background('./img/gamebg.png')
        self.images = pygame.sprite.Group()
        self.images.add(self.background)
        self.endgame = Button("./img/endgameclicked.png", "./img/endgame.png", 235, 300)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.endgame)
        
        # Music
        pygame.mixer.music.load("./sounds/winsong.wav")
        pygame.mixer.music.play(-1)

        # Text and Fonts
        self.titlefont = pygame.font.Font('./spacemission.otf', 60)
        self.title = self.titlefont.render("error", True, (40, 86, 155))
        self.scorefont = pygame.font.Font('./spacemission.otf', 30)
        self.score1 = self.scorefont.render("Player 1: 0", True, (125, 150, 245))
        self.score2 = self.scorefont.render("Player 2: 0", True, (125, 150, 245))
        
    def process_loop(self):
        """Runs code every game tick"""

        # Gets mouse inputs and position
        pygame.event.pump()
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Draws images and buttons
        self.images.draw(self.window)
        self.buttons.draw(self.window)

        # Draws text
        self.window.blit(self.score1, ((winx/12), (winy/12)))
        self.window.blit(self.score2, ((winx/20)*13, (winy/12)))

        # Draws text based on whether tie or win
        if self.text == "TIE!":
            self.window.blit(self.title, ((winx/12)*5, (winx/6)*2))
        else:
            self.window.blit(self.title, ((winx/30)*2, (winx/6)*2))
        
        # Checks buttons if they need to be hovered.
        for button in self.buttons:
            if button.check_mouse(mouse_pos):
                button.hover()
            else:
                button.unhover()

        # Checks if mouse is clicked. Runs button if so
        if mouse_state[0]:
            if self.endgame.check_mouse(mouse_pos):
                print("Clicked duo")
                self.endgame.click_sound()
                self.running = False

        # Checks if escape is pressed, returns to main menu.
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.endgame.click_sound()
            print("End game via escape")
            self.running=False
        
    def process_event(self, event):
        """For events"""
        pass