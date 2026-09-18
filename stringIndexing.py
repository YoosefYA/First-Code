credit_number = str(input("Please Enter your Credit card nunmber (XXXX-XXXX-XXXX-XXXX):"))

#Arrays follow the following algorithim:
#[ start : end : step ] note that the start is INclusive and the end is EXclusive

#The first four numbers
first_four = credit_number[:4]
print(f"Your Credit card number is {first_four}-XXXX-XXXX-XXXX")
#the last four numbers
last_four = credit_number[-4:]
print(f"Your Credit card number is XXXX-XXXX-XXXX-{last_four}")
#number in reverse
reverse_number = credit_number[::-1]
print(f"Your credit card number in reverse is {reverse_number}")