def sum_list(my_list):
    if not my_list:
        return 0
    else:
        first_element = my_list[0]
        rest_element = my_list[1:]
        return first_element + sum_list(rest_element)

numbers = [1,2,3,2,3,1]
result = sum_list(numbers)
print(result)