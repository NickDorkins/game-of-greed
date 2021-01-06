from collections import Counter
import random


class GameLogic:
  
 
#  Calculate score (Static method)
#  Inputs - Tuple
#  Outputs - Integer (Score Value)

    @staticmethod
    def calculate_score(kept_dice):
        counter = Counter(kept_dice)
        count = counter.most_common()
        scoring = 0

        if len(count) == 6:
            straight = True
            for die, freq in count:
               if freq != 1:
                   straight = False
            if straight == True:
                return 1500
           
        
        if len(count) == 3:
            pairs = True
            for die, freq in count:
                if freq == 2:
                    return 1500
                if freq != 2:
                    return 500                   
       
        all_scores = {
            (1, 1): 100,
            (1, 2): 200,
            (1, 3): 1000,
            (1, 4): 2000,
            (1, 5): 3000,
            (1, 6): 4000,
            (2, 1): 0,
            (2, 2): 0,
            (2, 3): 200,
            (2, 4): 400,
            (2, 5): 600,
            (2, 6): 800,
            (3, 2): 0,
            (3, 3): 300,
            (3, 4): 600,
            (3, 5): 900,
            (3, 6): 1200,
            (4, 2): 0,
            (4, 3): 400,
            (4, 4): 800,
            (4, 5): 1200,
            (4, 6): 1600,
            (5, 1): 50,
            (5, 2): 100,
            (5, 3): 500,
            (5, 4): 1000,
            (5, 5): 1500,
            (5, 6): 2000,
            (6, 2): 0,
            (6, 3): 600,
            (6, 4): 1200,
            (6, 5): 1800,
            (6, 6): 2400,
        } 

        for tup in count:
            if tup in all_scores:
                scoring += all_scores[tup]         
        return scoring 

        

     


        

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
 





