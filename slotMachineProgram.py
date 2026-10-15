import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for symbol in range(3) ]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")  

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


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
            continue

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"Yoe won ${payout}")
        else:
            print("Sorry you lost this round")

        play_again = input("Do you want to spin again? (Y/N): ")

        if play_again.upper() != 'Y':
            break
    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")
if __name__ == '__main__':
    main()