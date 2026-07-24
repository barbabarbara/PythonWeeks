# Task 2 — Explain It: Code Explanation

## Status

**Required**

## Instructions

Write a short explanation of how your calculator works. This can be written in the reflection field or submitted as a separate text file or shared link.

## Questions and Answers

### 1. What variables did you use, and what does each variable store?

The variable `first_number` stores the first number entered by the user.

The variable `second_number` stores the second number entered by the user.

The variable `operation` stores the arithmetic operation selected by the user, such as `+`, `-`, `*`, or `/`.

The variable `result` stores the result of the calculation performed on the two numbers.

### 2. Why do you need to convert input values using `float()` or `int()`?

The input values need to be converted using `float()` or `int()` because the `input()` function stores user input as a string by default.

Converting the values allows Python to treat them as numbers and perform arithmetic calculations.

Using `float()` also allows the calculator to work with decimal numbers, such as `4.5` or `10.75`.

### 3. How does your `if`, `elif`, and `else` structure decide which operation to run?

The `if` and `elif` statements decide which operation to run by checking the value stored in the `operation` variable.

Each condition compares the selected symbol with one of the supported operations:

- `+` for addition;
- `-` for subtraction;
- `*` for multiplication;
- `/` for division.

When one of the conditions is true, Python performs the calculation inside that block.

The final `else` block runs when the entered operation does not match any of the supported options.

### 4. How does your program handle division by zero?

Before performing division, the program checks whether `second_number` is equal to zero.

If the second number is zero, the program does not perform the division. Instead, it prints the following error message:

`Error: Division by zero is not allowed.`

This prevents the program from attempting an invalid mathematical operation.

### 5. How does your program handle an invalid operation?

If none of the `if` or `elif` conditions match the operation entered by the user, the final `else` block runs.

The program then prints:

`Invalid operation. Please choose +, -, *, or /.`

This tells the user that the selected operation is not supported.

### 6. Which part of your code shows that you understand the task?

Several parts of my code show that I understand the task.

I used `input()` to collect values from the user, converted the input values into numbers, provided four arithmetic operation choices, used conditional statements to select the correct calculation, handled invalid operations with a clear error message, and prevented division by zero.

The division check especially demonstrates my understanding because the program validates the second number before attempting the calculation.