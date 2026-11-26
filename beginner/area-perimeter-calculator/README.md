# Area and Perimeter Calculator

A command-line Python program that calculates the area and perimeter (or circumference) of a circle, triangle or rectangle.

**Level:** Beginner

## Learning objective

Practice building a simple menu with `if` / `elif` / `else`, validating input before calculating, and using basic geometry formulas in code.

## Features

- Asks which shape to use: circle, triangle or rectangle. Capital letters and extra spaces are ignored.
- **Circle:** reads the radius and prints the area and circumference.
- **Triangle:** reads the three sides and prints the area (using Heron's formula) and the perimeter.
- **Rectangle:** reads the length and width and prints the area and perimeter.
- Rejects values that are zero or negative, and rejects triangle sides that cannot form a triangle.
- Prints results rounded to two decimal places.

## Concepts demonstrated

- User input with `input()` and conversion to `float`
- String methods (`lower()`, `strip()`)
- `if` / `elif` / `else` menu with nested conditions
- Comparison and logical operators (`<=`, `or`)
- Input validation before calculating
- Arithmetic with `**` for powers and `** 0.5` for square roots
- Formatted output with f-strings (`:.2f`)

## How to run

Requires Python 3.

```bash
python area_perimeter_calculator.py
```

## Example usage

```text
Choose a shape (Circle/Triangle/Rectangle): triangle
Enter side a: 3
Enter side b: 4
Enter side c: 5
The area of triangle is 6.00 square units
The perimeter of triangle is 12.00 units
```

```text
Choose a shape (Circle/Triangle/Rectangle): triangle
Enter side a: 1
Enter side b: 1
Enter side c: 10
These sides cannot form a triangle!
```

## Bugs I found and fixed

- **Negative values were accepted.** A negative radius gave a normal-looking area, because squaring hides the sign, and a negative circumference. Each shape now checks the values first and only calculates when they are valid.
- **Rectangle check let one bad value through.** The condition used `and`, so only two bad values were rejected together. It now uses `or`.
- **Triangle area and perimeter could describe different triangles.** The first version asked for base and height for the area, and then asked for the sides separately for the perimeter. Now the triangle takes only the three sides and works out both from them. Heron's formula for the area is something I learned while fixing this.
- **Wrong unit label.** The rectangle perimeter said "square units"; it is now "units".

## Known limitations and possible improvements

- Typing something that is not a number (such as `abc`) crashes the program with a `ValueError`. It needs `try` / `except` handling.
- `pi` is set to `3.1416`, which is an approximation. The `math` module has a more precise value.
- The three shapes are written as separate blocks. Functions would make each shape easier to read and reuse.
- The program asks about one shape and then ends.
