from car import Car

car1 = Car("Mustang", 2026,"black", True)
car2 = Car("Corvet", 2025, "blue", False)
car3 = Car("Charger", 2024, "yellow", True)

print(car1.model) #The dot is called the attruibute accesses operator

car1.describe()
car2.drive()
car3.stop()