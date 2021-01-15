from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
# Creates empty dic to receive the auctions
auctions = {}
go_again = True

# Loops the process of adding new players for as many players as needed
while go_again:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    # Checks if the name entered already exists
    if name in auctions:
        print("The name you've entered already exists. Please chose a different one.")
    else:
        auctions[name]=bid
        decision = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if decision == "no":
            go_again = False
        clear()
        
# Checks who the winner is and what his bid is.
winning_bid = 0
winning_player = ""

for player in auctions:
    score = auctions[player]
    if score > winning_bid:
        winning_bid = score
        winning_player = player

# If two players have the same bid, the first one to place it will win.
# Prints out the final statement
print(f"The winner is {winning_player} with a bid of ${winning_bid}")