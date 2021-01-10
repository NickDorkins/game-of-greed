from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
import sys


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

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()


    def decline_game(self):
        print("OK. Maybe another time")


    def start_game(self,remaining_dice=6):

        if not self.round_num:
            self.round_num += 1
            print(f"Starting round {self.round_num}")
        

        print(f"Rolling {remaining_dice} dice...")

        display_tuple = self._roller(remaining_dice)

        display_dice = ' '.join(str(num) for num in display_tuple)            

        print(f'*** {display_dice} ***')

        if not GameLogic.calculate_score(display_tuple):
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")

            print(f"You banked 0 points in round {self.round_num}")

            print(f"Total score is {self.banker.balance} points")

            self.banker.clear_shelf()

            self.round_num += 1
            print(f"Starting round {self.round_num}")
            self.start_game()

        #found the below solution on stackoverflow https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
        
        user_input = input("Enter dice to keep, or (q)uit:\n> ")
    
        if user_input == "q":  
            print(f'Thanks for playing. You earned {self.banker.balance} points')    
            sys.exit()
        else:
            user_input = list(user_input)
            for num in range(len(user_input)):
                user_input[num] = int(user_input[num]) 

            user_input = tuple(user_input)
            validate_user_input = GameLogic.validate_keepers(display_tuple, user_input)


            while not validate_user_input:
                print("Cheater!!! Or possibly made a typo...")
                print(f'*** {display_dice} ***')

                user_input = input("Enter dice to keep, or (q)uit:\n> ")
                user_input = list(user_input)
                user_input = user_input.remove(' ')
                print(user_input)

                for num in range(len(user_input)):
                    user_input[num] = int(user_input[num])

                user_input = tuple(user_input)    
                validate_user_input = GameLogic.validate_keepers(display_tuple, user_input)
                print(validate_user_input)
            remaining_dice =  remaining_dice - len(user_input)

        scoreLogic = GameLogic.calculate_score(user_input)

        self.banker.shelf(scoreLogic)

        

        print(f"You have {self.banker.shelved} unbanked points and {remaining_dice} dice remaining")

        roll_bank_or_quit = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

        if roll_bank_or_quit == "r":

            if not remaining_dice:
                self.start_game()

            self.start_game(remaining_dice)
        
        elif roll_bank_or_quit == "b":
            # if rolled dice is in user_input: validated 
            # Using "in"
            # send the data to the banker line107/108    
            shelf = self.banker.shelved
            self.banker.bank()

            print(f"You banked {shelf} points in round {self.round_num}")

            print(f"Total score is {self.banker.balance} points")

            self.round_num += 1
            print(f"Starting round {self.round_num}")
            self.start_game()

        elif user_input == "q":
            print(f'Thanks for playing. You earned {self.banker.balance} points')    
            sys.exit() 



if __name__ == "__main__":
    game = Game()
    game.play()