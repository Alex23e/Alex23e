import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 50)
attempts = 5

while attempts > 0:
    print(f"\nYou have {attempts} attempts left.")
    guess = int(input("Guess a number between 1 and 50: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the right number!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a higher number.")
    else:
        print("📈 Too high! Try a lower number.")
       
    attempts -= 1

if attempts == 0:
    print(f"\nGame Over! The correct number was {secret_number}.")
