def find_max(my_list):
    max_value = my_list[0] #set as initiative value for maximum
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value

my_list = [1, 20, 213, 21, 354, 454, 3444, 1]
max_value = find_max(my_list)
print(f"The maximum value in the 1D is {max_value}")

def find_max_2D(my_list):
    max_value = my_list[0][0]
    for row in my_list:
        for element in row:
            if element > max_value:
                max_value = element
    return max_value

def find_max_2D_V2(my_list):
    max_value = my_list[0][0]
    for i in range(len(my_list)):
        i = my_list[i]
        for x in range(len(i)):
            x = int(i[x])
            if x > max_value:
                max_value = x
    return max_value


my_list = [[1,2,31],
           [4,15,6],
           [17,8,2]]
for row in my_list:
    for element in row:
        print(element, end=" ")
    print()


max_value = find_max_2D(my_list)
print(f"The maximum value in the 2D is {max_value}")

my_list = [[1,2,71],
           [4,65,6],
           [17,81,2]]

max_value = find_max_2D_V2(my_list)
print(f"The maximum value in the 2D is {max_value}")