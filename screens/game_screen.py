import pygame
from .base_screen import Screen
from models import Ball, Paddle, Button, Background
from constants import LIMITS, WINDOW_HEIGHT as winy, WINDOW_WIDTH as winx
import time

class GameScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Values to pass back/return
        self.lost = False
        self.current_score = [0, 0]
        self.ai = True
        self.close = False

        # Create objects
        self.ball = Ball()
        self.ball.launch()
        self.p1 = Paddle("left")
        self.p2 = Paddle("right")
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.p1, self.p2)

        # Music and sounds
        pygame.mixer.music.load("./sounds/music.wav")
        pygame.mixer.music.play(-1)
        self.bounce = pygame.mixer.Sound("./sounds/pop.wav")
        self.over = pygame.mixer.Sound("./sounds/lose.wav")
        self.quitrounds = Button("./img/quitclicked.png", "./img/quit.png", int(winx/2.307), int((winy/6)*4))
        self.endround = Button("./img/roundclicked.png", "./img/round.png", int(winx/2.55319), int(winy/1.27659))

        # Buttons, Background, Fonts
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.endround, self.quitrounds)
        self.background = Background('./img/gamebg.png')
        self.images = pygame.sprite.Group()
        self.images.add(self.background)
        self.scorefont = pygame.font.Font('./spacemission.otf', int((winx+winy)/60))
        self.scores = self.scorefont.render("Scores", True, (125, 150, 245))


    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass

    

    def round_end(self):
        """Displays ROUND OVER text after ball is off limits"""
        self.titlefont = pygame.font.Font('./spacemission.otf', int((winx+winy)/16))
        self.title = self.titlefont.render("Round Over", True, (125, 150, 245))
        self.window.blit(self.title, ((winx/20)*3, (winy/6)))
        


    def process_loop(self):
        """Runs code every tick"""
        # Update the ball position
        self.ball.update()

        # Update the paddles' positions
        self.paddles.update()

        # Draws images, buttons, and fonts
        self.images.draw(self.window)
        self.window.blit(self.scores, (int((winx/20) * 9), int(winy/30)))
        self.window.blit(self.score1, (int(winx/2.55319), int(winy/30)))
        self.window.blit(self.score2, ((int(winx/10)*6), int(winy/30)))
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

        # Checks if the ball needs to be deflected.
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
        

        # Checks if the ball is off limits.
        if self.ball.off_limits:
            #Plays the lost round sound effect once.
            if self.lost == False:
                self.lost = True
                pygame.mixer.Sound.play(self.over)
            
            # Draws images
            self.round_end()
            self.buttons.draw(self.window)

            # Checks for inputs
            pygame.event.pump()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.endround.click_sound()
                print("End round via spacebar")
                self.running=False
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.quitrounds.click_sound()
                self.close = True
                print("End round via escape")
                self.running=False

            # Checks mouse state and position
            mouse_state = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.check_mouse(mouse_pos):
                    button.hover()
                else:
                    button.unhover()
            if mouse_state[0]:
                # Runs the end round button, starts next round
                if self.endround.check_mouse(mouse_pos):
                    self.endround.click_sound()
                    print("Ending Round")
                    self.running = False

                # Runs the end game button, opens menu
                if self.quitrounds.check_mouse(mouse_pos):
                    self.quitrounds.click_sound()
                    print("Ending Round")
                    self.close = True
                    self.running = False
            
            # Updates the score.
            if self.ball.rect.x < (LIMITS["right"] // 2):
                self.p1.score = 1
            else:
                self.p2.score = 1
            return True

        return False

