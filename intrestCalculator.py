princaple = float(input("Please input your princaple: "))
rate = float(input("Please input the interest rate: "))
peroids = float(input("Please input the number of full years of the investement: "))

final = princaple*(1+rate/100)^peroids
print(final)