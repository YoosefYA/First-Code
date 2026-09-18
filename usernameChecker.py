
while True:
    user_name = str(input("Please Input your username: "))

    if len(user_name) > 12:
        print("Username can't be longer than 12 characters long")
    elif user_name.count(" ") > 0:
        print("Please don't use spaces in the username")
    elif user_name.isalpha() == False:
        print("Please don't use numbers or symbols in the username")
    else:
        print("Thank you for entering a valid username")
        break

    print("Try again")