# Employee Profile Formatter

A small Python script that builds and prints an employee profile from sample data, using string concatenation, f-strings and slicing.

**Level:** Beginner

## Learning objective

Practice working with strings: joining them, converting numbers to text, formatting output and slicing parts out of a code.

## Features

- Builds a full name from a first and last name.
- Prints sentences about the employee's age and experience.
- Prints a one-line employee card with name, age, position, salary and address.
- Extracts parts of the employee code `DEV-2026-JD-001`: the first three characters (`DEV`), the year (`2026`), the initials (`JD`) and the last three characters (`001`).

The script uses made-up sample data (John Doe), set directly in the code.

## Concepts demonstrated

- Variables and string concatenation (`+`, `+=`)
- Converting numbers to text with `str()`
- f-strings
- String indexing and slicing, including negative indexes (`[-3:]`)
- Printing output with `print()`

## How to run

Requires Python 3.

```bash
python employee_profile_formatter.py
```

## Example output

```text
John Doe is 28 years old
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000 | Address: 123 Main Street, Apartment 4B
DEV
2026
JD
001
```

## Known limitations and possible improvements

- All values are written directly in the code. Reading them with `input()` would make it a real profile generator.
- The code slices fixed positions, so it only works for codes with exactly this format.
- The output lines could be grouped into a function once I've learned functions.
