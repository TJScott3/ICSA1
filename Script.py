import random

secret = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
print("Try to guess it!")

# Start with a placeholder guess
guess = 0

# Loop until the guess is correct
while guess != secret:
    text = input("Your guess: ")
    guess = int(text)

    # Give hints
    if guess < secret:
        print("Too low.")
    if guess > secret:
        print("Too high.")
    if guess == secret:
        print("That's right!")
        print("You win!")

print("Thanks for playing!") 
