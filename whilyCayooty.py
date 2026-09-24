food = input("Please enter your favourite food (press q t quit): ")

while not food == "q":
    print("Your favourite food is", food)
    food = input("Please enter your other favourite food (press q t quit): ")

print("Goodebye")

num = int(input("Please enter a # from 1 to 10: "))

while num < 1 or num > 10:
    print("Please try again")
    num = int(input("Please enter a # from 1 to 10: "))

print(f"Your number is {num}")