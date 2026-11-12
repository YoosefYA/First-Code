
class Car:

    wheels = 4 #these variables are called class because they are 
#               outside the constructor which are shared amongst all objects created from this class

    def __init__(self, model, year, color, for_sale): #__init__ is called a constructor
        self.model = model #these variables are called instance variables because they are created inside the constructor
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.model} {self.color} {self.year}")