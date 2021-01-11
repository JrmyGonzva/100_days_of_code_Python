#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")
# Gets the three variables needed with the correct datatypes
bill_as_float = float(input("What was your total bill? $"))
percentage_as_int = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_as_int = int(input("How many people to split the bill?"))

# Calculate the total tips
total_tip = bill_as_float * percentage_as_int / 100
#Calculate the total bill, including tips
bill_with_tips = total_tip + bill_as_float
#Calculate the amount to pay per person, rounding the 2 decimal
tip_per_person = round(bill_with_tips / people_as_int,2)
#printing the final amount, making sure to have a 2 decimal number
message = f"Each person should pay: ${tip_per_person:.2f}"
print(message)

