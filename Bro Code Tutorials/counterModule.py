import time

user_input = int(input("Enter how long you want your timer to be (in seconds): "))

for x in range(user_input, 0, -1):

    seconds = x % 60
    minutes = int( x / 60 ) % 60
    hours = int( x / 3600 )
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP")