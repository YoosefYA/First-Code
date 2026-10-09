foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press q to exit): ")
    if food.lower() == 'q':
        break
    price = float(input(f"Enter the price of a {food}: $"))
    prices.append(price) 
    foods.append(food)

print("-----Your Cart-----")
for i in foods:
    print(i, end=" ")

for x in prices:
    total += x

print()
print(f"Your total = ${total}")
