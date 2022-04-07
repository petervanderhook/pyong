import pygame
from .base_screen import Screen
from models import Ball, Paddle, Button, Background
from constants import LIMITS
import time

class GameScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Create objects
        self.ball = Ball()
        self.ball.launch()
        self.lost = False
        self.current_score = [0, 0]
        self.ai = True
        self.p1 = Paddle("left")
        self.p2 = Paddle("right")
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.p1, self.p2)
        pygame.mixer.music.load("./sounds/music.wav")
        pygame.mixer.music.play(-1)
        self.bounce = pygame.mixer.Sound("./sounds/pop.wav")
        self.over = pygame.mixer.Sound("./sounds/lose.wav")
        self.endround = Button("./img/roundclicked.png", "./img/round.png", 235, 400)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.endround)
        self.background = Background('./img/gamebg.png')
        self.images = pygame.sprite.Group()
        self.images.add(self.background)
        self.scorefont = pygame.font.Font('./spacemission.otf', 20)
        self.scores = self.scorefont.render("Scores", True, (40, 86, 155))


    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass
    def play_sound(self, sound):
        pygame.mixer.Sound.play(self.bounce)
        pygame.mixer.music.stop()

    

    def round_end(self):
        self.titlefont = pygame.font.Font('./spacemission.otf', 75)
        self.title = self.titlefont.render("Round Over", True, (40, 86, 155))
        self.window.blit(self.title, (90, 100))
        

    def get_score(self):
        return [self.p1.score, self.p2.score]

    def process_loop(self):
        self.images.draw(self.window)
        self.window.blit(self.scores, (270, 20))
        self.window.blit(self.score1, (235, 20))
        self.window.blit(self.score2, (360, 20))
        # Update the ball position
        self.ball.update()

        # Update the paddles' positions
        self.paddles.update()

        # Blit everything
        self.paddles.draw(self.window)
        self.window.blit(self.ball.image, self.ball.rect)

        # Player 1 Movement
        if pygame.key.get_pressed()[pygame.K_w]:
            self.p1.up()
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.p1.down()

        # Player 2 movement (only if self.ai = False)
        if self.ai == False:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.p2.up()
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                self.p2.down()
        else:
            ball_height = self.ball.image.get_height()
            ball_y = self.ball.rect.y + (ball_height / 2)
            self.p2.check_move(ball_y, self.ball.off_limits)


        if pygame.Rect.colliderect(self.ball.rect, self.p1.rect):
            if (self.ball.off_limits == False): 
                print("P1 DEFLECTS!")
                self.ball.rect.x += 10
                self.ball.bounce("right")
                pygame.mixer.Sound.play(self.bounce)


        if pygame.Rect.colliderect(self.ball.rect, self.p2.rect):
            if (self.ball.off_limits == False): 
                print("P2 DEFLECTS!")
                self.ball.rect.x -= 10
                self.ball.bounce("left")
                pygame.mixer.Sound.play(self.bounce)
        
        if self.ball.off_limits:
            if self.lost == False:
                pygame.mixer.Sound.play(self.over)
                self.lost = True
            self.round_end()
            self.buttons.draw(self.window)
            pygame.event.pump()
            mouse_state = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.check_mouse(mouse_pos):
                    button.hover()
                else:
                    button.unhover()
            if mouse_state[0]:
                if self.endround.check_mouse(mouse_pos):
                    self.endround.click_sound()
                    print("Ending Round")
                    self.running = False
            
            if self.ball.rect.x < (LIMITS["right"] // 2):
                self.p1.score = 1
            else:
                self.p2.score = 1
            return True

        return False

