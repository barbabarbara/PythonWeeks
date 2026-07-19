"""
Week 1 — Part 3: Debugging a Broken Calculator

This file contains:

1. The original broken code.
2. An explanation of the problems.
3. A corrected calculator function.
4. Automatic test cases.
"""


# ---------------------------------------------------------
# Original broken code
# ---------------------------------------------------------

BROKEN_CODE = """
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

print("Result:", result)
"""


# ---------------------------------------------------------
# Problems found
# ---------------------------------------------------------

DEBUGGING_NOTES = """
Problems in the original code:

1. input() returns strings, not numbers.
2. If the user enters 10 and 5, addition produces "105".
3. Only the + operation is implemented.
4. result is undefined if the user chooses -, *, /, or another symbol.
5. Division by zero is not handled.
6. Invalid operations are not handled.
"""


# ---------------------------------------------------------
# Corrected calculation logic
# ---------------------------------------------------------

def calculate(first_number, second_number, operation):
    """
    Perform one arithmetic calculation.

    Returns:
        A number when the operation is valid.
        An error message when the operation is invalid.
    """

    if operation == "+":
        return first_number + second_number

    elif operation == "-":
        return first_number - second_number

    elif operation == "*":
        return first_number * second_number

    elif operation == "/":
        if second_number == 0:
            return "Error: Division by zero is not allowed."

        return first_number / second_number

    else:
        return "Error: Invalid operation. Choose +, -, *, or /."


# ---------------------------------------------------------
# Interactive program
# ---------------------------------------------------------

def run_calculator():
    """Ask the user for input and display the result."""

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    operation = input("Choose operation (+, -, *, /): ").strip()

    result = calculate(first_number, second_number, operation)

    print("Result:", result)


# ---------------------------------------------------------
# Automatic tests
# ---------------------------------------------------------

def run_tests():
    """Run several test cases for the corrected calculator."""

    test_cases = [
        (10, 5, "+", 15),
        (10, 5, "-", 5),
        (10, 5, "*", 50),
        (10, 5, "/", 2),
        (10, 0, "/", "Error: Division by zero is not allowed."),
        (10, 5, "%", "Error: Invalid operation. Choose +, -, *, or /."),
    ]

    print("\nRunning automatic tests...\n")

    for first_number, second_number, operation, expected in test_cases:
        actual = calculate(first_number, second_number, operation)

        if actual == expected:
            status = "PASS"
        else:
            status = "FAIL"

        print(
            f"{status}: "
            f"{first_number} {operation} {second_number} "
            f"= {actual!r}, expected {expected!r}"
        )


# ---------------------------------------------------------
# Main menu
# ---------------------------------------------------------

def main():
    """Choose between the interactive calculator and tests."""

    print(DEBUGGING_NOTES)

    print("Choose an option:")
    print("1. Run the corrected calculator")
    print("2. Run automatic tests")
    print("3. Display the original broken code")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        run_calculator()

    elif choice == "2":
        run_tests()

    elif choice == "3":
        print("\nOriginal broken code:")
        print(BROKEN_CODE)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()