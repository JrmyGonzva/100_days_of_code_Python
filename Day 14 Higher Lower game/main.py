from art import logo, vs
from game_data import data
from replit import clear
import random

# Creates initial variables
score = 0
still_winning = True
# Creates a_index outside of the while loop, as a will take the value of b for the next round.
a_index = random.randint(1, len(data)-1)

print(logo)
#while we are still winning, continue playing
while still_winning:
    b_index = random.randint(1, len(data)-1)
    #Checks that both characters are different
    while a_index == b_index:
        b_index = random.randint(1, len(data)-1)

    character_a = data[a_index]
    character_b = data[b_index]

    # Prints the character's description
    print(f"Compare A: {character_a['name']}, a {character_a['description']}, from {character_a['country']}")

    print(vs)

    print(f"Againt B: {character_b['name']}, a {character_b['description']}, from {character_b['country']}")
    # Asks the user for his/her choice
    choice = input("Who has more followers? 'a' or 'b'?").lower()

    followers_a = character_a['follower_count']
    followers_b = character_b['follower_count']
    # Checks who the winning letter is
    winning_letter = ''
    if followers_a >= followers_b:
        winning_letter = 'a'
    else:
        winning_letter = 'b'
    # Checks if the user is correct
    if choice != winning_letter:
        # If wrong, calculates final score and exits the loop
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score {score}.")
        still_winning = False
    else:
        # If right, clears the screen, add 1 to the score and assigns b to a.
        clear()
        score +=1
        print(logo)
        print(f"You are right! Current score {score}.")
        a_index = b_index
