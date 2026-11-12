print("--------- MENU ---------")

menu = {"hotdog":4.00,
        "popcorn":1.50,
        "soda":2.00,
        "nachos":4.50,
        "french fries":2.50,
        "chips":1.00,
        "juice":3.00,
        "water":0.75}

cart =[]
total = 0

for key, value in menu.items():
    print(f"{key:12}: ${value:.2f}")

print("-------------------------")

while True:
    food = input("Select an item (q to quite): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- Your Order ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")