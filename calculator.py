from calculator_art import logo

def add_values(a, b):
    return a + b

def subtract_values(a, b):
    return a - b

def multiply_values(a, b):
    return a * b

def divide_values(a, b):
    return a / b

actions = {
    "+": add_values,
    "-": subtract_values,
    "*": multiply_values,
    "/": divide_values
}

def reset_screen():
    print("\n" * 50)

def start_calculator():
    print(logo)

    first_number = float(input("Enter the first number: "))
    for symbol in actions:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Choose an operation: ")
        next_number = float(input("Enter the next number: "))
        operation_function = actions[operation_symbol]
        result = operation_function(first_number, next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {result}")

        if input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation: ") == 'y':
            first_number = result
        else:
            continue_calculation = False
            reset_screen()
            start_calculator()

start_calculator()