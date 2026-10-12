def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():

    global balance
    while True:
        amount = str(input("Enter an amount to be deposited: "))
        if amount.isdigit() is True:
            amount = int(amount)
            if amount >= 0:
                    balance += int(amount)
                    break
        else:
            print("Invalid Input")


def withdraw():

    global balance
    while True:
        amount = str(input("Enter an amount to be withdrawed: "))
        if amount.isdigit() is True:
            amount = int(amount)
            if amount >= 0:
                    balance -= int(amount)
                    break
        else:
            print("Invalid Input")

balance = 0
is_running = True

while is_running:
    print("---------------------")
    print("Banking program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("---------------------")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid Input")

print("Thank you! Have a nice day!") 