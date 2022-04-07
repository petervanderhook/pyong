import pygame
from models import Background, Button
from .base_screen import Screen


class EndScreen(Screen):

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)
        pygame.init()
        self.background = Background('./img/gamebg.png')
        self.images = pygame.sprite.Group()
        self.images.add(self.background)
        self.text = "error"
        self.endgame = Button("./img/endgameclicked.png", "./img/endgame.png", 235, 300)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.endgame)
        pygame.mixer.music.load("./sounds/winsong.wav")
        pygame.mixer.music.play(-1)
        self.titlefont = pygame.font.Font('./spacemission.otf', 60)
        self.title = self.titlefont.render("error", True, (40, 86, 155))
        self.scorefont = pygame.font.Font('./spacemission.otf', 30)
        self.score1 = self.scorefont.render("Player 1: 0", True, (125, 150, 245))
        self.score2 = self.scorefont.render("Player 2: 0", True, (125, 150, 245))
        
    def process_loop(self):
        pygame.event.pump()
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        self.images.draw(self.window)
        self.buttons.draw(self.window)
        self.window.blit(self.score1, (50, 50))
        self.window.blit(self.score2, (390, 50))
        print(self.text)
        if self.text == "TIE!":
            self.window.blit(self.title, (250, 200))
        else:
            self.window.blit(self.title, (40, 200))
        
        for button in self.buttons:
            if button.check_mouse(mouse_pos):
                button.hover()
            else:
                button.unhover()
        if mouse_state[0]:
            if self.endgame.check_mouse(mouse_pos):
                print("Clicked duo")
                self.endgame.click_sound()
                self.running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.endgame.click_sound()
            print("End round via spacebar")
            self.running=False
        
    def process_event(self, event):
        pass