
while True:
    unit = str(input("Please input the current temperature unit (C, F): "))
    curr_temp = float(input("Please input the temperature: "))

    if unit == "C":
        new_temp = round((curr_temp * 9) / 5 + 32, 1)
        print(f"{curr_temp}C is equivelint to {new_temp}F")
        break
    elif unit == "F":
        new_temp = round((curr_temp - 32 ) * 5 / 9, 1)
        print(f"{curr_temp}F is equivelint to {new_temp}C")
        break
    else:
        print(f"Please input a valit temperature unit, not {unit}")

print("Thank you for using this application")