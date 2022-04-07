import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen

def update_score(current_score, new_scores):
    current_score[0] += new_scores[0]
    current_score[1] += new_scores[1]
    return current_score

def game_start():
    pass
    

def main():
    score = [0, 0]
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen = MenuScreen(window)
    #screen = GameScreen(window)
    #screen.ai = True
    result = screen.loop()
    
    if result:
        print("The ball went off limits, play again")
        print(score)
        screen2 = GameScreen(window)
        screen2.loop()
        score = update_score(score, screen2.get_score())
        print(score)
    else:
        print("Ball was still in play, quit")


if __name__ == "__main__":
    main()  
    pygame.mixer.init()
