#Task 1
try:
    numerator = float(input("Enter the numerator: "))
    divisor = float(input("Enter the divisor: "))
    total = numerator / divisor
    print(f"{numerator} / {divisor} = {total:.2f}")
except ZeroDivisionError:
    print("You shall not do it")

#Task 2
try:
    num = int(input("Please input an integer: "))
    print(f"Your number is {num}")
except ValueError:
    print("You shall not do it")

#Task 3
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("You shall not do it")
except IOError:
    print("You shall not do it")