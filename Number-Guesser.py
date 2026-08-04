import random

print("===== NUMBER GUESSING GAME =====")

print("Choose Difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    maximum = 50
elif choice == 2:
    maximum = 100
elif choice == 3:
    maximum = 500
else:
    print("Invalid choice. Defaulting to Medium.")
    maximum = 100

number = random.randint(1, maximum)
attempts = 0

print(f"\nI have chosen a number between 1 and {maximum}.")
print("Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.\n")

    elif guess > number:
        print("Too high! Try again.\n")

    else:
        print("\n🎉 Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break