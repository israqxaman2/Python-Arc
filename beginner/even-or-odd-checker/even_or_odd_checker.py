number = float(input("Enter an integer: "))
if number % 1 == 0:
    number = int(number)
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
else:
    print(number, "is not a whole number")
