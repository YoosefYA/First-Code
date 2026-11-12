for x in range (1, 11):
    print("I love you", x,"times")

for i in reversed(range(1, 11)):
    print(i)
print("HAPPY NEW YEAR!!!")

print("Let's count in twos")
for z in range(0, 11, 2):
    print(z)

print("I heard that 13 is unlucky so lets skip it when we count")
for count in range(1, 21):
    if count == 13:
        print("we don't count this one")
        continue
    else:
        print(count)