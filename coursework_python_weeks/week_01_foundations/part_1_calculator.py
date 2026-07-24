# Ask the user to enter two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Ask the user to choose an arithmetic operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the selected calculation
if operation == "+":
    result = first_number + second_number
    print(f"The result is: {result}")

elif operation == "-":
    result = first_number - second_number
    print(f"The result is: {result}")

elif operation == "*":
    result = first_number * second_number
    print(f"The result is: {result}")

elif operation == "/":
    # Prevent division by zero
    if second_number != 0:
        result = first_number / second_number
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation. Please choose +, -, *, or /.")