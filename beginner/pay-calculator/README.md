# Weekly Pay Calculator

A command-line Python program that calculates weekly pay from hours worked and an hourly rate, including overtime, tax and take-home pay.

**Level:** Beginner

## Learning objective

Practice conditional logic (`if` / `elif` / `else`, including nested conditions), validating user input, and formatting numbers in output.

## Features

- Asks for the hours worked and the hourly rate.
- Rejects invalid input with a message: negative hours or rate, zero hours, or more than 168 hours (the number of hours in a week).
- Pays the normal rate for the first 40 hours and 1.5x the rate for every hour beyond 40.
- Applies tax to the total pay: 10% if the total is 1000 or less, 20% if it is more.
- Prints regular pay, overtime pay, total pay, tax and take-home pay, rounded to two decimal places.

## Concepts demonstrated

- User input with `input()` and conversion to `float`
- Arithmetic operators
- Comparison and logical operators (`<`, `<=`, `>`, `==`, `or`)
- `if` / `elif` / `else` chains and nested conditions
- Input validation using conditions
- Formatted output with f-strings (`:.2f`)

## How to run

Requires Python 3.

```bash
python pay_calculator.py
```

## Example usage

```text
Enter hours: 50
Enter rate per hour: 20
Your Regular pay: 800.00 $
Your Overtime pay: 300.00 $
Your total pay: 1100.00 $
Tax: 220.00 $
Your take-home pay: 880.00 $
```

```text
Enter hours: 200
Enter rate per hour: 10
Do not lie!
```

## Bugs I found and fixed

- **Crash on invalid input:** The tax step ran even after an error message, but `total` had not been created yet, which caused a `NameError`. The pay and tax code now only runs when the input is valid.
- **Exactly 1000 skipped the tax:** The tax rules checked `< 1000` and `> 1000`, so a total of exactly 1000 matched neither. The second check is now a plain `else`.
- **Overtime paid twice:** Hours beyond 40 were counted at the normal rate and then again at 1.5x. Regular pay now covers only the first 40 hours.

## Known limitations and possible improvements

- Typing something that is not a number (such as `abc`) crashes the program with a `ValueError`. It needs `try` / `except` handling.
- The tax rule is a simplified flat rule applied to the whole total, not real tax brackets. As a result, earning slightly more than 1000 can leave less take-home pay (1000 gives 900.00, but 1001 gives 800.80).
- The pay and tax output lines are repeated in several places. Functions would remove that duplication.
