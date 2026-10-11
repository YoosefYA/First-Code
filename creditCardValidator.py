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

#step 3 double every