###Functions for adding elements

my_list = [1,2,3]
#append() adds an element to the end of the list
my_list.append(4)
print(my_list)
#insert() adds an element at a specific index
my_list.insert(1,5)
print(my_list)

###Functions for removing elements

my_list = [10,20,30,40,50]
#remove() removes the first occurrence of a specific value
my_list.remove(30)
print(my_list)
#pop() removes and returns the element at a pecific index
popped_element = my_list.pop(1)
print(popped_element)
#del reomves an element at a specific index or a slice of elements
del my_list[0]
print(my_list)
del my_list[:]
print(my_list)

###Other useful functions

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
#sort() sorts the list in ascending order 
