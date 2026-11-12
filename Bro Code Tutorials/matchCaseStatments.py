def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not valid day"
def is_weekend(day):
    match day:
        case "It is Sunday" | "It is Saturday":
            return True
        case "It is Monday" | " It is Tuesday" | "It is Wednesday" | "It is Thursday" | "It is Friday":
            return False
        case _:
            return False

day = int(input("Enter the day from 1-7: "))
print(f"{day_of_week(day)} and it is a {is_weekend(day_of_week(day))} weekend")