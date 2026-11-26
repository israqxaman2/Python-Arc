hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
if hours < 0 or rate < 0:
    print("Hours and rate must be positive!")
elif hours == 0:
    print("You did not put any work this week.")
elif hours > 168:
    print("Do not lie!")
else:
    if hours <= 40:
       pay = hours * rate
       overtime = 0
       total = pay + overtime
       print(f"Your Regular pay: {pay:.2f} $")
       print(f"Your Overtime pay: {overtime:.2f} $")
       print(f"Your total pay: {total:.2f} $")
    else:
       pay = 40 * rate
       overtime = (hours - 40)*1.5*rate 
       total = pay + overtime
       print(f"Your Regular pay: {pay:.2f} $")
       print(f"Your Overtime pay: {overtime:.2f} $")
       print(f"Your total pay: {total:.2f} $")

    if total <= 1000:
       tax = 0.1* total
       total -= tax
       print(f"Tax: {tax:.2f} $")
       print(f"Your take-home pay: {total:.2f} $")
    else :
       tax = 0.2*total
       total -= tax
       print(f"Tax: {tax:.2f} $")
       print(f"Your take-home pay: {total:.2f} $")

    
