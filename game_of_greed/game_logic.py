
from collections import Counter
import random


class GameLogic:
    
  

#  Calculate score (Static method)

    @staticmethod
    def roll_dice(num_die):
        diceroll = []
        for die in range(1, num_die + 1):
            add_score = random.randint(1, 6) 
            diceroll.append(add_score)
            # print(add_score)
    
        return tuple(diceroll)







test = GameLogic()
print(test.roll_dice(6))
 



        
        
 
#  Inputs - Tuple
#  Outputs - Integer (Score Value)


#  Roll Dice (Static Method)
#  Input - Integer (1 -6)
#  Output - Tuple (List of face value per dice)

