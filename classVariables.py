class Student:

    class_year = 2028 #Class variables
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age 
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidwards", 40)

print(student1.name)
print(student2.age)
print()
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")