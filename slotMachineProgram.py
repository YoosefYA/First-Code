def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    print("*************************")
    print(" Welcome to Python slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        try:
            bet = float(input("Place your bet:  "))
        except ValueError:
            print("Invalid Input")

        if bet > balance:
            print("You cannot bet nire than you own")
if __name__ == '__main__':
    main()