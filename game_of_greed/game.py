from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.round_num = 0

        # self._roller =  GameLogic.roll_dice()

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    # Application should allow user to set aside dice each roll
    # Application should allow “banking” current score or rolling again.
    # Application should keep track of total score
    # Application should keep track of current round
    
    def start_game(self):
        self.round_num += 1
        self.current_die_rolled = 6

        print(f"Starting round {self.round_num}")
        print(f"Rolling {self.current_die_rolled} dice...")

        display_tuple = list(GameLogic.roll_dice(self.current_die_rolled))

        for  num in display_tuple:
            str(num)
        print(display_tuple)
        display_dice = ' '.join(display_tuple)
        print(f'*** {display_dice} ***')
            
           

if __name__ == "__main__":
    game = Game()
    game.play()