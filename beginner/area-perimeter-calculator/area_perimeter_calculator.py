shape = input("Choose a shape (Circle/Triangle/Rectangle): ").lower().strip()

if shape == "circle":
    radius = float(input("Enter the radius of circle: "))
    if radius <= 0:
        print("Radius must be positive!")
    else:
        pi = 3.1416 
        area = pi * (radius ** 2)
        circumference = 2*pi*radius
        print(f"The area of circle: {area:.2f} square units")
        print(f"The circumference of circle: {circumference:.2f} units")
elif shape == "triangle":
        a =float(input("Enter side a: "))
        b =float(input("Enter side b: "))
        c =float(input("Enter side c: "))
        if a <= 0 or b<= 0 or c<= 0 :
             print("Sides must be positive!")
        elif a + b <= c or a + c <= b or b + c <= a:
             print("These sides cannot form a triangle!")
        else:
            perimeter = a+b+c 
            s = perimeter/2 
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 
            print(f"The area of triangle is {area:.2f} square units")
            print(f"The perimeter of triangle is {perimeter:.2f} units")

elif shape == "rectangle" :
        length =float(input("Enter the length of rectangle: "))
        width =float(input("Enter the width of rectangle: "))
        if length <= 0 or width <= 0:
            print("Please enter valid inputs!")
        else:
            area = width * length
            perimeter = 2* (length + width)
            print(f"The area of the rectangle is {area:.2f} square units")
            print(f"The perimeter of the rectangle is {perimeter:.2f} units")
else :
    print("Choose circle/triangle/rectangle")


