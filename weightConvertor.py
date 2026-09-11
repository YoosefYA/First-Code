unit = str(input("Enter the current weight's unit (lb, kg):"))
weight = float(input("Enter the weight:"))

if unit == "lb":
    con_weight = weight * 0.453592
    print(f"{weight} lb is equal to {con_weight} kg")
elif unit == "kg":
    con_weight = weight * 2.20462
    print(f"{weight} kg is equal to {con_weight} lb")
else:
    print("Invalid unit. Please enter either 'lb' or 'kg'.")