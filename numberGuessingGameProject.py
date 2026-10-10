import random

low = 1
high = 100
answer = random.randint(low, high)
guess_count = 0

is_running = True

print("Python Number Guessing Game")
print(f"select a number between {low} - {high}")
while is_running:
    guess = input("Enter your guess: ")

    if guess.isalpha():
        print("Input invalid")
        print(f"Please select a number between {low} - {high}")
    else:
        guess = int(guess)
        guess_count += 1
        if guess < low or guess > high:
            print("That number is out of range")
            print(f"Please select a number between {low} - {high}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"Correct! The answer was {guess}")
            print(f"Number of guesses: {guess_count}")
            is_running = False