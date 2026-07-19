# Week 1 — Python Foundations and GPT Learning Habits

## Main Task: Five-Part Python Foundations Task

Complete the five parts below. The goal is not only to build a working calculator, but also to demonstrate:

- how you reason about Python code;
- how you explain your solution;
- how you identify and correct errors;
- how ChatGPT influenced your learning process.

This week establishes an early baseline that can later be compared with the no-AI withdrawal weeks.

## Weekly Task Structure

This week is divided into five clear parts.

Complete all required parts first. Part 5 is an optional challenge for participants who want a stronger programming task after completing the core work.

---

## Part 1 — Build Something: Simple Calculator

**Status:** Required

Create a Python program that works as a simple calculator. The program should let the user enter two numbers and choose one arithmetic operation.

### Requirements

Your program must:

- ask the user to enter the first number;
- ask the user to enter the second number;
- convert the input values to numbers using `float()` or `int()`;
- ask the user to choose an operation: `+`, `-`, `*`, or `/`;
- use `if`, `elif`, and `else` to decide which calculation to perform;
- calculate and print the result;
- handle division by zero with a clear error message;
- handle an invalid operation with a clear message;
- use clear variable names;
- include short comments explaining the most important parts.

### Suggested File

`part_1_calculator.py`

### Example Output

```text
Enter first number: 10
Enter second number: 5
Choose operation (+, -, *, /): +

Result: 15
```

---

## Part 2 — Explain It: Code Explanation

**Status:** Required

Write a short explanation of how your calculator works.

Submit the explanation in:

`part_2_explanation.md`

### Questions

1. What variables did you use, and what does each variable store?
2. Why do you need to convert input values using `float()` or `int()`?
3. How does your `if`, `elif`, and `else` structure decide which operation to perform?
4. How does your program handle division by zero?
5. How does your program handle an invalid operation?
6. Which part of your code best demonstrates that you understand the task?

---

## Part 3 — Debug Something: Broken Calculator Code

**Status:** Required

Study the broken code below. Explain what is wrong and how it should be corrected.

### Broken Code

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

print("Result:", result)
```

### Questions

1. What is wrong with this code?
2. What happens if the user enters `10` and `5`?
3. Why is `num1 + num2` not safe in this program?
4. How should the input values be converted?
5. Which arithmetic operations are missing?
6. What other error handling should be added?
7. What happens if the user chooses an operation other than `+`?
8. How would you correct the program?

### Suggested File

Place the corrected code and your debugging comments in:

`part_3_debugging.py`

---

## Part 4 — Reflect on ChatGPT Use

**Status:** Required

Write honestly about how you used ChatGPT during this week.

The purpose is to understand whether ChatGPT supported:

- learning;
- explanation;
- debugging;
- verification;
- full-solution generation.

Submit the reflection in:

`part_4_chatgpt_reflection.md`

### Questions

1. Did you ask ChatGPT for hints, explanations, debugging help, verification, or a complete solution?
2. Which ChatGPT answer helped you understand the task best?
3. Did you copy any code directly?
4. If you copied code, did you understand it afterward?
5. Could you now explain the calculator without ChatGPT?
6. Could you recreate the calculator without ChatGPT?
7. What would you try independently before asking ChatGPT next time?
8. At what point did you decide to ask ChatGPT instead of continuing independently?
9. Did ChatGPT help you understand the code, or mainly help you finish it?
10. Which parts of the final solution are clearly your own work?

---

## Part 5 — Optional Challenge for Stronger Learners

**Status:** Optional

After completing the required parts, choose one or more optional challenges.

These challenges are not required, but they can demonstrate stronger problem-solving, program structure, and code quality.

### Optional Challenge Choices

You may:

- allow the user to repeat calculations until they type `quit`;
- create functions such as `add()`, `subtract()`, `multiply()`, and `divide()`;
- use `try` and `except` to handle invalid number input;
- store previous calculations in a list;
- print the calculation history;
- allow the user to choose whether to continue or exit after each calculation;
- separate input, calculation, and output into different functions;
- add validation so that only supported operations are accepted.

### Suggested File

`part_5_optional_challenge.py`

---

## Expected Weekly Files

Your Week 1 folder should contain:

```text
week_01_foundations/
├── README.md
├── part_1_calculator.py
├── part_2_explanation.md
├── part_3_debugging.py
├── part_4_chatgpt_reflection.md
└── part_5_optional_challenge.py
```

---

## Suggested Steps

1. Create the file `part_1_calculator.py`.
2. Build the basic calculator.
3. Test addition.
4. Test subtraction.
5. Test multiplication.
6. Test division.
7. Test division by zero.
8. Test an invalid operation, such as `%`.
9. Write your explanation in `part_2_explanation.md`.
10. Study the broken calculator code.
11. Explain what is wrong with it.
12. Correct the broken code in `part_3_debugging.py`.
13. Complete the ChatGPT reflection in `part_4_chatgpt_reflection.md`.
14. Complete one or more optional challenges if desired.
15. Test all Python files before submission.
16. Save and commit your completed work to GitHub.

---

## How You May Use ChatGPT This Week

You may use ChatGPT during this week.

Try to use it as a learning tool rather than immediately requesting a complete solution.

### Recommended Uses

You may ask ChatGPT to:

- explain `input()`;
- explain `float()` and `int()`;
- explain variables;
- explain `if`, `elif`, and `else`;
- explain division-by-zero handling;
- help you understand an error message;
- provide a hint;
- review code you have already attempted;
- explain why a particular solution works;
- compare two possible solutions.

For the debugging task, first try to identify the problems independently before asking ChatGPT.

### Good Prompt Example

```text
I am learning Python. Do not give me the full answer immediately.

Guide me through building a simple calculator step by step.

Help me understand input(), float(), variables, if/elif/else,
invalid-operation handling, and division-by-zero handling.

After each step, ask me to explain what the code does.
```

### ChatGPT Log Guidance

Save only ChatGPT conversations that are relevant to this weekly task.

Before submitting the log:

- remove private information;
- remove unrelated conversations;
- include the prompts you wrote;
- include the relevant answers you received;
- keep the sequence of the interaction clear.

---

## Required Submission

Submit the following:

- completed Part 1 calculator code;
- Part 2 written explanation;
- completed Part 3 debugging task;
- Part 4 ChatGPT-use reflection;
- Part 5 optional challenge, if completed;
- relevant ChatGPT interaction log;
- confidence rating from 1 to 5;
- dependency rating from 1 to 5;
- total time used in minutes.

### Confidence Rating

Rate how confident you feel about completing a similar task independently.

| Rating | Meaning              |
|--------|----------------------|
| 1      | Not confident        |
| 2      | Slightly confident   |
| 3      | Moderately confident |
| 4      | Confident            |
| 5      | Very confident       |

### Dependency Rating

Rate how dependent you felt on ChatGPT during the task.

| Rating | Meaning |
|---|---|
| 1 | Completed almost entirely independently |
| 2 | Needed minor assistance |
| 3 | Needed moderate assistance |
| 4 | Needed substantial assistance |
| 5 | Could not complete the task without ChatGPT |

---

## Completion Checklist

### Required Parts

- [ ] Part 1 — Calculator completed
- [ ] Part 1 — Addition tested
- [ ] Part 1 — Subtraction tested
- [ ] Part 1 — Multiplication tested
- [ ] Part 1 — Division tested
- [ ] Part 1 — Division by zero tested
- [ ] Part 1 — Invalid operation tested
- [ ] Part 2 — Code explanation completed
- [ ] Part 3 — Problems in the broken code explained
- [ ] Part 3 — Corrected debugging code completed
- [ ] Part 4 — ChatGPT reflection completed
- [ ] Relevant ChatGPT log prepared
- [ ] Confidence rating submitted
- [ ] Dependency rating submitted
- [ ] Time used submitted

### Optional Part

- [ ] Part 5 — Optional challenge completed

---

## Learning Goals

By the end of this week, you should be able to:

- receive input from a user;
- convert text input into numeric values;
- store information in variables;
- use conditional statements;
- perform arithmetic calculations;
- handle division by zero;
- respond to invalid operations;
- identify basic errors in Python code;
- explain how your own program works;
- reflect on how ChatGPT affected your learning and problem-solving.