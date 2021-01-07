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

    # Application should allow user to set aside dice each roll
    # Application should allow “banking” current score or rolling again.
    # Application should keep track of total score
    # Application should keep track of current round
    
    def start_game(self):
        self.round_num += 1
        self.current_die_rolled = 6


        print(f"Starting round {self.round_num}")
        print(f"Rolling {self.current_die_rolled} dice...")

        display_tuple = self._roller(self.current_die_rolled)
        #found the below solution on stackoverflow https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
        display_dice = ' '.join(str(num) for num in display_tuple) 
        print(f'*** {display_dice} ***')
    
        user_input = input("Enter dice to keep, or (q)uit:\n> ")
    
        if user_input == "q":  
            print(f'Thanks for playing. You earned {self.banker.balance} points')    
            sys.exit()
        else:
            user_input = list(user_input)
            for num in range(len(user_input)):
                user_input[num] = int(user_input[num]) 

        user_input = tuple(user_input)
        remaining =  self.current_die_rolled - len(user_input)

        scoreLogic = GameLogic.calculate_score(user_input)

        self.banker.shelf(scoreLogic)
        print(f"You have {self.banker.shelved} unbanked points and {remaining} dice remaining")

        roll_bank_or_quit = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

        if roll_bank_or_quit == "r":
           
           GameLogic.roll_dice(remaining)

           print(f"Rolling {remaining} dice...")

           display_tuple = GameLogic.roll_dice(remaining)

           #found the below solution on stackoverflow https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python

           display_dice = ' '.join(str(num) for num in display_tuple)

           print(f'*** {display_dice} ***')

           user_input = input("Enter dice to keep, or (q)uit:\n> ")

           if user_input == 'q' or user_input == "quit":
                print('Goodbye')    
                sys.exit()
           else:
               user_input = list(user_input)
               for num in range(len(user_input)):
                   user_input[num] = int(user_input[num])

           user_input = tuple(user_input)
           remaining =  self.current_die_rolled - len(user_input)

           scoreLogic = GameLogic.calculate_score(user_input)

           self.banker.shelf(scoreLogic)
           print(f"You have {self.banker.shelved} unbanked points and {remaining} dice remaining")
        
        elif roll_bank_or_quit == "b":
            shelf = self.banker.shelved
            self.banker.bank()

            print(f"You banked {shelf} points in round {self.round_num}")

            print(f"Total score is {self.banker.balance} points")

            self.start_game()

        elif user_input == "q" or user_input == "quit":
            print(f'Thanks for playing. You earned {self.banker.balance} points')    
            sys.exit() 


if __name__ == "__main__":
    game = Game()
    game.play()