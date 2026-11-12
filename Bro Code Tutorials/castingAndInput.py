print("Welcome to the supermarket!")

item = input("What would you like to buy?")
price = float(input(f"What is the price of one {item}?"))
quantity = int(input("How many would you like to buy?"))

total = float(price * quantity)

print(f"You are buying {quantity} x {item}. The total cost is ${total:.2f}.")