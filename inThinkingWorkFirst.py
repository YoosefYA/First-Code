age = 18
name = "Yoosef"
print(name,age)

price = 17.68
integer_price = int(price)
print(price,integer_price)

global_count = 0

def increment_count():
    global global_count
    global_count += 1

increment_count()
increment_count()
print(global_count)
