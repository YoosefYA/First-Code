start_programme = "r"
while True:
    #starting mechanisim that loops until the user wants it to stop
    start_programme = input("Do you want to start the programme? (yes/no): ")
    start_programme = start_programme.lower()
    if start_programme == "no":
        break

    principal = float(input("Please input your principal: ")) #original amount
    rate = float(input("Please input the interest rate (%): "))

    #Convert rate to decimal
    rate = (rate + 100) / 100
    peroids = float(input("Please input the number of full years of the investement: "))
    x = 1 #For counting 

    #Main algorithim
    while x <= peroids:
        principal = principal*rate
        x += 1

    print(f"Your new budget is {principal}")

print("Thank you for using this application!!")