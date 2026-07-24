# Task 5: Improved Calculator Program

# 1. Arithmetic functions

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


# 2. Input-validation functions

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    valid_operations = ["+", "-", "*", "/"]

    while True:
        operation = input(
            "Choose an operation (+, -, *, /): "
        ).strip()

        if operation in valid_operations:
            return operation

        print("Invalid operation. Please choose +, -, *, or /.")


def get_menu_choice():
    valid_choices = ["1", "2", "3", "4"]

    while True:
        choice = input("Choose an option: ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please select 1, 2, 3, or 4.")


# 3. Calculation logic

def calculate(number1, number2, operation):
    if operation == "+":
        return add(number1, number2)

    if operation == "-":
        return subtract(number1, number2)

    if operation == "*":
        return multiply(number1, number2)

    if operation == "/":
        return divide(number1, number2)


# 4. Calculation and history functions

def perform_calculation(history):
    first_number = get_number("Enter the first number: ")
    operation = get_operation()
    second_number = get_number("Enter the second number: ")

    if operation == "/" and second_number == 0:
        print("Error: Division by zero is not allowed.")
        return

    result = calculate(first_number, second_number, operation)

    calculation = (
        f"{first_number} {operation} "
        f"{second_number} = {result}"
    )

    history.append(calculation)

    print(f"\nResult: {result}")


def show_history(history):
    if not history:
        print("\nNo calculations yet.")
        return

    print("\nCalculation history:")

    for position, calculation in enumerate(history, start=1):
        print(f"{position}. {calculation}")


def clear_history(history):
    if not history:
        print("\nThe calculation history is already empty.")
        return

    history.clear()
    print("\nCalculation history cleared.")


# 5. Menu display

def show_menu():
    print("\n==============================")
    print("          CALCULATOR")
    print("==============================")
    print("1. New calculation")
    print("2. Show history")
    print("3. Clear history")
    print("4. Exit")


# 6. Main program

def main():
    calculation_history = []

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            perform_calculation(calculation_history)

        elif choice == "2":
            show_history(calculation_history)

        elif choice == "3":
            clear_history(calculation_history)

        elif choice == "4":
            print("\nCalculator closed.")
            break


# 7. Program starting point

if __name__ == "__main__":
    main()