#Step 0 initiat variables

sum_odd_digits = 0
sum_even_digits = 0
total = 0
card_num = input("Enter the cridet card number: ")

#Step 1 Remove "-" and " "

card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]

#step 2 add every second digit from right to left

for x in card_num[::2]:
    sum_odd_digits += int(x)

#step 3 double every second digit from right to left if the result is a two digit number add the two numbers together to get a single digit number and then add them up

for x in card_num[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1 + (x%10))
    else:
        sum_even_digits += x

#step 4 add the two sums you found together:

total = sum_even_digits + sum_odd_digits

#step 5 if the total is divvisable by ten print valid 

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")