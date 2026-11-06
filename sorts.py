def bubble_sort(arr):
    counter = 0
    n = len(arr)
    flag = 0
    for i in range(n -1):

        for j in range (n - i -1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
            counter += 1
        
        if flag == 0:
            return print(f"{arr} is already sorted.")

    return print(f"{counter} steps, new array = {arr}")  

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return print(arr)

bubble_numbers = [10, 35, 21, -23, 26, 13, 78, 95]
bubble_sort(bubble_numbers)
print()

bubble_sorted_numbers = [1, 2 , 3, 4, 5, 6, 7, 8]
bubble_sort(bubble_sorted_numbers)
print()

selection_numbers = [10, 35, 21, -23, 26, 13, 78, 95]
selection_sort(selection_numbers)
