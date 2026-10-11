import random
#ASKI art components
# ● ┌ ─ ┐ │ └ ┘
#"┌─────────┐"
#"│         │"
#"│         │"
#"│         │"
#"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│      ●  │",
        "│         │",
        "│  ●      │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│      ●  │",
        "│    ●    │",
        "│  ●      │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0

while True:
    num_of_dice = input("How many dice would you like to throw?: ")
    if num_of_dice.isdigit():
        num_of_dice = int(num_of_dice)
        break
    else:
        print("Invalid input")

for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

while True:
    display_type = input("Do you want it to be displayed Horizontally?(y/n): ").lower()
    if display_type != "y" and display_type != "n":
        print("Invalid Input")

    #Horizental Display
    elif display_type == "y":
        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end="")
            print()
        break

    #Vertical Display
    else:
        for die in range(num_of_dice):
            for line in dice_art.get(dice[die]):
                print(line)
        break

for die in dice:
    total += die
print(f"Total = {total}")
