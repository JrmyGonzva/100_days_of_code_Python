import replit
from art import logo

print(logo)
# Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    should_continue = True

    num1 = float(input("What's the first number? "))

    while should_continue:
        for operation in operations:
            print(operation)
            
        operation_symbol = input("Pick an operation from the line above. ")
        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        decision = input(f"Do you want to continue with {answer}? Type 'y' to continue or 'n' to start a new calculation.")
        if decision == "n":
            should_continue = False
            replit.clear()
            calculator()
        else:
            num1 = answer

calculator()
