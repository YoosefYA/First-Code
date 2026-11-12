s = "Programming"

end = s[3:]

middle = s[3:7]

print(end)
print(middle)

p = "Banana"
p = p.replace("a","o")
print(p)

email = input("Please enter your email: ")
goodindex = email.find("@")
print(f"Your email username is {email[:goodindex]}")
print(f"Your domain is {email[goodindex + 1 :]}")