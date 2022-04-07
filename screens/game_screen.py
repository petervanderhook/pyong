import pygame
from .base_screen import Screen
from models import Ball, Paddle
from constants import LIMITS

class GameScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Create objects
        self.ball = Ball()
        self.ball.launch()
        self.p1 = Paddle("left")
        self.p2 = Paddle("right")
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.p1, self.p2)
        pygame.mixer.music.load("./sounds/music.wav")
        pygame.mixer.music.play(-1)
        self.sound = pygame.mixer.Sound("./sounds/pop.wav")

    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass
    def play_sound(self, sound):
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()

    def get_score(self):
        return [self.p1.score, self.p2.score]

    def process_loop(self):
        # Update the ball position
        self.ball.update()

        # Update the paddles' positions
        self.paddles.update()

        # Blit everything
        self.paddles.draw(self.window)
        self.window.blit(self.ball.image, self.ball.rect)

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.p2.up()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.p2.down()
        if pygame.key.get_pressed()[pygame.K_w]:
            self.p1.up()
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.p1.down()


        if pygame.Rect.colliderect(self.ball.rect, self.p1.rect):
            if (self.ball.off_limits == False): 
                print("P1 DEFLECTS!")
                self.ball.rect.x += 10
                self.ball.bounce("right")
                pygame.mixer.Sound.play(self.sound)


        if pygame.Rect.colliderect(self.ball.rect, self.p2.rect):
            if (self.ball.off_limits == False): 
                print("P2 DEFLECTS!")
                self.ball.rect.x -= 10
                self.ball.bounce("left")
                pygame.mixer.Sound.play(self.sound)

        if self.ball.off_limits:
            if self.ball.rect.x < (LIMITS["right"] // 2):
                self.p1.score = 1
            else:
                self.p2.score = 1
            return True

        return False

