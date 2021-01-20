import random
from replit import clear
game_again = True


def guessing():
    print("Welcome to the number guessing game!\n")
    print("I'm thinking of a number between 1 and 100")
    DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if DIFFICULTY =='easy':
        LIVES = 10
    elif DIFFICULTY == 'hard':
        LIVES = 5
    else: 
        print("You did not chose a correct difficulty.")
    lives_remaining = LIVES
    ANSWER = random.randint(1,100)
    continue_guessing = True
    while continue_guessing:
        print(f"You have {lives_remaining} lives to guess the number.")
        
        guess = int(input ("Make a guess: "))
        if ANSWER == guess:
            print(f"Congrats, the number to find was {ANSWER} and you found it!")
            continue_guessing = False
            
        else:
            lives_remaining -= 1
            if lives_remaining == 0:
                print("You run out of lives, sorry. Game Over")
                continue_guessing = False
            elif ANSWER < guess:
                print(f"Too high, try again.\n")
            elif ANSWER > guess:
                print(f"Too low, try again.\n")
        
    go_again = input("Do you want to play again? Type 'y' or 'n'. ")
    clear()
    if go_again =='n':
        return False


while game_again == True:
    guessing()
    if guessing() == False:
        game_again = False