principal = float(input("Please input your principal: "))
rate = float(input("Please input the interest rate: "))
peroids = float(input("Please input the number of full years of the investement: "))
result = 0
x = 1
while x <= peroids:
    principal = principal*rate
    x += 1

print(f"Your new budget is {principal}")