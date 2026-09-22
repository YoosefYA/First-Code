x = 1

def calculator():
    global x
    
    operator = input("Enter an operator (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        x = 0
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        x = 0
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        x = 0
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else :
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            x = 0
    else:
        print("invalid operator. Please enter one of the following: +, -, *, /")

while x == 1:
    calculator()
print("Thank you for using the calculator!")
#what is the difference between global and local 