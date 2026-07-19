````markdown
# Task 3 — Debug Something: Broken Calculator Code

## Status

**Required**

## Instructions

Look at the broken calculator code below. Explain what is wrong and how it should be fixed.

## Broken Code

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

print("Result:", result)
```

## Questions and Answers

### 1. What is wrong with this code?

The code does not convert the input values into numbers.

The `input()` function returns strings, so `num1` and `num2` are stored as text rather than numeric values.

The code also only supports addition. It does not include subtraction, multiplication, or division.

Another problem is that `result` is only created when the user enters `+`. If the user chooses another operation, the program reaches the final `print()` statement before `result` has been assigned. This causes an error.

### 2. What happens if the user enters `10` and `5`?

If the user enters `10` and `5` and chooses `+`, Python joins the two strings together.

The result becomes:

`105`

instead of:

`15`

This happens because the values are still strings.

### 3. Why is `num1 + num2` not safe here?

`num1 + num2` is not safe because `input()` returns strings.

When the `+` operator is used with strings, Python joins them instead of performing mathematical addition.

For example:

```python
"10" + "5"
```

produces:

```text
105
```

This creates an incorrect result without necessarily showing an error message.

### 4. How should the input values be converted?

The input values should be converted using `float()` or `int()`.

For example:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

Using `float()` is more flexible because it allows the calculator to work with both whole numbers and decimal numbers.

For example, it can accept values such as:

- `10`
- `5.5`
- `-3.25`

### 5. What operations are missing?

The broken code only supports addition.

The following operations are missing:

- subtraction using `-`;
- multiplication using `*`;
- division using `/`.

The program should use `if`, `elif`, and `else` to handle all four supported operations.

### 6. What other error handling should be added?

The program should handle division by zero.

Before dividing, it should check whether the second number is zero.

For example:

```python
if num2 == 0:
    print("Error: Division by zero is not allowed.")
```

The program should also handle invalid operations.

If the user enters an unsupported operation, such as `%`, the program should display a clear message.

For example:

```python
print("Invalid operation. Please choose +, -, *, or /.")
```

It would also be useful to handle invalid number input using `try` and `except`, although this may be considered an optional improvement for this task.

## Corrected Code

```python
# Convert the user's input into numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an arithmetic operation
operation = input("Choose operation (+, -, *, /): ")

# Perform the selected calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    # Prevent division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operation. Please choose +, -, *, or /.")
```

## Summary

The main problems in the broken code are that the input values are stored as strings, only addition is supported, `result` may be undefined, division by zero is not handled, and invalid operations are not handled.

The corrected version converts the input values using `float()`, supports all four arithmetic operations, checks for division by zero, and displays a clear message when the user enters an invalid operation.
````
