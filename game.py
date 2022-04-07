import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen
from screens.end_screen import EndScreen

def game_start():
    pass
    

def main():
    # Sets score to 0, 0 and initializes pygame and display.
    score = [0, 0]
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Creates game screen
    game = MenuScreen(window)
    menu_used = game.loop()
    # Sets the rounds from the value set in the game
    rounds = game.gamestate[0]

    # Sets ai bool.
    ai = game.gamestate[1]

    # if game.practice is True, runs the practice games
    if game.practice:
        # Practice runs infinitely until quit.
        while game.practice:
            # Makes a new game window
            game = GameScreen(window)
            game.current_score = score
            # Updates score, passed in externally to the game before the loop begins so as to keep the score values outside of the screen.
            game.score1 = game.scorefont.render(f"{score[1]}", True, (125, 150, 245))
            game.score2 = game.scorefont.render(f"{score[0]}", True, (125, 150, 245))
            # Sets ai to the ai bool
            game.ai = ai

            # runs the game
            result = game.loop()

            # updates the score values based on the game results
            score[0] += game.p1.score
            score[1] += game.p2.score
            print("Current Score", score)



    # If not practice, game runs by default
    while game.close == False:
        # Only runs the game to the round limit
        for i in range(0, rounds):
            if game.close:
                break
            # Makes a new game window if game wasnt toggled to close.
            game = GameScreen(window)
            # Updates scores and sets the text to be blit in the screen parameters
            game.current_score = score
            game.score1 = game.scorefont.render(f"{score[1]}", True, (125, 150, 245))
            game.score2 = game.scorefont.render(f"{score[0]}", True, (125, 150, 245))

            # sets ai bool
            game.ai = ai
            # runs game loop
            result = game.loop()
            # updates scores
            score[0] += game.p1.score
            score[1] += game.p2.score
            print("Current Score", score)
        break
    
    # Runs end game screen if the game wasn't closed.
    if game.close == False:
        # Creates end scree 
        end = EndScreen(window)
        
        # Gets winner or tie and adds to a string
        if score[0] > score[1]:
            title_string = "Player 2 \nWinner!"
        elif score[0] < score[1]:
            title_string = "Player 1 \nWinner!"
        else:
            title_string= "TIE!"
        
        # Writes title string result to a parameter and adds those to the screen parameters score1 and score2
        end.title = end.titlefont.render(title_string, True, (40, 86, 155))
        end.text = title_string
        end.score1 = end.scorefont.render(f"P1\nScore: {score[1]}", True, (125, 150, 245))
        end.score2 = end.scorefont.render(f"P2\nScore: {score[0]}", True, (125, 150, 245))

        # Runs the game loop
        end_result = end.loop()



if __name__ == "__main__":
    # Loops the game forever until closed
    while True:
        main()
