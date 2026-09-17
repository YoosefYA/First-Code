while True:
    is_student =str(input("Are you a student? (yes/no):"))
    is_student = is_student.lower()
    #comment on nothing cuz why not -_-
    if is_student == "yes":
        print("Welcome to UWC CSC!")
        break
    else:
        print("Access denied")

print("Thank you for trying this application!")