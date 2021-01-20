############### Blackjack Project #####################
from art import logo
from replit import clear
import random


#Flag to start a new game
should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def calculate_score(player_cards):
    """This function calculate the score for either the player or the dealer, depending on the argument."""
    score = sum(player_cards)
    return score

def ace_degrade(player_cards, player_score):
    """This function will change the value of the ace from 11 to 1 if the score is greater than 21"""
    if '11' in player_cards and player_score > 21:
        for card in player_cards:
            position_11 = player_cards.index('11')
        player_cards[position_11] = 1

def display_during_game(status):
    """This function display the user cards and the dealer cards at the moment of the game chosen: either during the game or at the end."""
    if status == 'game':
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")
    elif status == 'end':
        print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

def adding_card():
        """This function adds a card for the user if requested. It goes on to calculate the winner of the game"""
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card =='y':
            #Adds another card to the user and calculates its score
            user_cards.append(random.choice(cards))
            ace_degrade(user_cards,calculate_score(user_cards))
            calculate_score(user_cards)
            user_score = calculate_score(user_cards)
            #score > 21, ends the game
            if user_score > 21:
                display_during_game("end")
                print("You went over. You lose")
                another_card ='n'    
            #score <= 21 continue the game       
            else:
                display_during_game("game")
                adding_card()
        

while should_continue == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    clear()
    print(logo)

    #creates empty lists to receive users and computer cards   
    user_cards = []
    dealer_cards =[]

    #Adds 2 cards to the user and the dealer
    for player in range(2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    display_during_game("game")     
                
    adding_card()

    if calculate_score(user_cards) <= 21:
        #cheks if computer values is < 17 to add another card 
        while calculate_score(dealer_cards)<17:
            dealer_cards.append(random.choice(cards))
            ace_degrade(dealer_cards,calculate_score(dealer_cards))
        #display final hands.
        display_during_game("end")
        #Works out who the winner is
        if calculate_score(user_cards) ==21:
            print("You win with Blackjack!")
        elif (calculate_score(user_cards) > calculate_score(dealer_cards)) or calculate_score(dealer_cards) > 21 :
            print("You win!")
        elif calculate_score(user_cards) == calculate_score(dealer_cards):
            print("It's a draw")
        else: 
            print("You lose.")

            
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    



############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## We only see one card from the dealer
## We can see all of our cards
## Draw if our cards values = dealer cards values
## At the end, if the dealer cards values < 17, he must take another card
