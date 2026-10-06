divisor = int(input("Input the number you want to devide 10 by: "))
try:
    result = float(10/divisor)
    print(f"10/{divisor} = {result:.2f}")
except ZeroDivisionError:
    print("You cannot devide by zero")
finally:
    print("Thanks for trying this program")