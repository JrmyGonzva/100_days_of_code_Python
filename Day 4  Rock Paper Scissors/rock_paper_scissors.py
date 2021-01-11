rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
images = [rock, paper, scissors]
#Getting variables for my choice and computer choice
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

#Printing my ascii art
if my_choice >= 3 or my_choice < 0:
  print("You've typed an invalid number, you lose.")
else:
  print(images[my_choice])

  #printing the computer's ascii art
  print("\n\nComputer chose\n")
  print(images[computer_choice])

  #determining the winner
  if my_choice == computer_choice:
    print("It's a draw. Try again.")
  elif my_choice == computer_choice + 1 or (my_choice == 0 and computer_choice == 2):
    print("You win, congrats!")
  else: 
    print("Sorry, you've lost.")
