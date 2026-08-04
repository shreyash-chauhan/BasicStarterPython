import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = ""

if input("Include letters? (y/n): ").lower() == "y":
    characters += string.ascii_letters

if input("Include numbers? (y/n): ").lower() == "y":
    characters += string.digits

if input("Include symbols? (y/n): ").lower() == "y":
    characters += string.punctuation

if len(characters) == 0:
    print("Error! You must choose at least one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)