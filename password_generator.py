#Password Generator Project
import random

#Generating the lists of possibles characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Getting the variables of strength and repetitions
print("Welcome to the PyPassword Generator!\n")
number_passwords = int(input("How many passwords to you want to generate?\n"))
strength = input("\nHow strong do you want your password to be? \nType \"weak\", \"medium\" or \"strong\"\n").lower()

#Checking validity of inputs
if (strength != "weak") and (strength !="medium") and (strength !="strong"):
  print("You've typed an invalid strength. Try again.")
else:
  print("\n") #Adding a new line after the inputs
  number_of_repetitions = 0
  #Repeating the loops, as many times as requested 
  while number_of_repetitions < number_passwords:
    password = ""
    number_of_repetitions += 1
    #Generating passwords with appropriate strength
    if strength =="weak":
      nr_letters = random.randint(6,8)
      nr_numbers = random.randint(1,2)
      nr_symbols = 0
    elif strength =="medium":
      nr_letters = random.randint(8,10)
      nr_numbers = random.randint(4,6)
      nr_symbols = random.randint(2,5)
    else: 
      nr_letters = random.randint(10,15)
      nr_numbers = random.randint(6,10)
      nr_symbols = random.randint(5,15)
      
    #Getting letters in password, as many times as the user requested it
    for letter in range(1, nr_letters +1 ):
      password += random.choice(letters)

    #Getting symbols in password
    for symbol in range(1, nr_symbols +1):
      password += random.choice(symbols)

    #Getting numbers in password
    for number in range(1, nr_numbers +1):
      password += random.choice(numbers)

    #Placing the password into a list to shuffle it
    # ---------------LIST--------------
    password_list =[] 
    for char in password:
      password_list += char

    #shuffling the list
    random.shuffle(password_list)

    password_shuffled = ""
    for char in password_list:
      password_shuffled += char
    print(f"Your #{number_of_repetitions} {strength} password is: {password_shuffled}")



#----------- LIST ------------
# # ----------STRING ------------
# #Shuffles the password around, as a string
# shuffled_password = ''.join(random.sample(password, len(password)))

# #Print final password
# print(shuffled_password)
