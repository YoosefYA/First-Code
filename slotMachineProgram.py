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
            bet = int(input("Place your bet: "))
        except ValueError:
            print("Invalid Input")
if __name__ == '__main__':
    main()