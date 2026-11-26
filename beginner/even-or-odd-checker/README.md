# Even or Odd Checker

A small command-line Python program that tells you whether a number is even, odd, or not a whole number.

**Level:** Beginner

## Learning objective

Practice the modulo operator (`%`) and nested `if` / `else` conditions.

## Features

- Asks for a number.
- Prints whether a whole number is even or odd.
- Reports when the number is not a whole number, such as `3.5`.
- Works with negative numbers and zero.

## Concepts demonstrated

- User input with `input()` and conversion to `float`
- Converting a float to an integer with `int()`
- The modulo operator (`%`), used to test divisibility
- Nested `if` / `else` conditions

## How to run

Requires Python 3.

```bash
python even_or_odd_checker.py
```

## Example usage

```text
Enter an integer: 7
7 is odd
```

```text
Enter an integer: 3.5
3.5 is not a whole number
```

## Known limitations and possible improvements

- Typing something that is not a number (such as `abc`) crashes the program with a `ValueError`. It needs `try` / `except` handling.
- The program checks one number and then ends. A loop would let it keep asking.
