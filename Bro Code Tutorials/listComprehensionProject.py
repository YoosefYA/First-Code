doubles = []
for x in range(1, 11):
    doubles.append(x*2)

print(doubles)

#or you can do it this way
#[expression / for / value / in / iterable / if condition]

triples = [x* 3 for x in range(1,11)]
print(triples)

fruites = ["apples", "oranges", "banana", "pineapple"]
fruites_upper = [fruite.upper() for fruite in fruites]

print(fruites_upper)

numbers = [1, -2, 3, -4, 5, -6]
numbers_pos = [number for number in numbers if number > 0]

print(numbers_pos)