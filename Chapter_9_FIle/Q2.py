#the game() function in a program lets a user play a game and returns the score as an integr. You need to read 'Hi-score.txt'
# which is either blank or contains the 

import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    #fetch the  hisscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
           hiscore =0    

    print(f"Your score: {score}")
    if(score> hiscore ):
        #write this  hiscore to the file
        with open("hiscore.txt", "w") as f:  
            f.write(str(score))

    return score            


game()