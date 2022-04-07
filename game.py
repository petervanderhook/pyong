import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen
from screens.end_screen import EndScreen

def game_start():
    pass
    

def main():
    score = [0, 0]
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game = MenuScreen(window)
    menu_used = game.loop()
    rounds = game.gamestate[0]
    ai = game.gamestate[1]
    if game.practice:
        while game.practice:
            game = GameScreen(window)
            game.current_score = score
            game.score1 = game.scorefont.render(f"{score[1]}", True, (125, 150, 245))
            game.score2 = game.scorefont.render(f"{score[0]}", True, (125, 150, 245))
            game.ai = ai
            game
            result = game.loop()
            score[0] += game.p1.score
            score[1] += game.p2.score
            print("Current Score", score)



    # Value in score array represent goals they have let past.
    while game.close == False:
        for i in range(0, rounds):
            if game.close:
                break
            game = GameScreen(window)
            game.current_score = score
            game.score1 = game.scorefont.render(f"{score[1]}", True, (125, 150, 245))
            game.score2 = game.scorefont.render(f"{score[0]}", True, (125, 150, 245))
            game.ai = ai
            game
            result = game.loop()
            score[0] += game.p1.score
            score[1] += game.p2.score
            print("Current Score", score)
        break
    
    if game.close == False:
        end = EndScreen(window)
        if score[0] > score[1]:
            title_string = "Player 2 \nWinner!"
        elif score[0] < score[1]:
            title_string = "Player 1 \nWinner!"
        else:
            title_string= "TIE!"
        end.title = end.titlefont.render(title_string, True, (40, 86, 155))
        end.text = title_string
        end.score1 = end.scorefont.render(f"P1\nScore: {score[1]}", True, (125, 150, 245))
        end.score2 = end.scorefont.render(f"P2\nScore: {score[0]}", True, (125, 150, 245))
        end_result = end.loop()



if __name__ == "__main__":
    while True:
        main()
    pygame.mixer.init()
