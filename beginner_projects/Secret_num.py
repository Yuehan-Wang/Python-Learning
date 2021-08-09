import random

def guess(x):
    num = random.randint(1, x)
    guess = 0
    while guess != num:
        guess = int(input(f"Between 1 and {x}, Your Guess: "))
        if guess < num:
            print("too small")
        elif guess > num:
            print("too large")
    print(f"{num} solved!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "correct" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too small or too large, or correct? ")
        if feedback == "too large":
            high = guess - 1
        if feedback == "too small":
            low = guess + 1
    print(f"{guess} is the number!")

computer_guess(10)