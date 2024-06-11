import string
import random


def password_generator(Length, use_Letters, use_Numbers, use_Symbols):
    characters = ""
    if use_Letters:
        characters += string.ascii_letters
    if use_Numbers:
        characters += string.digits
    if use_Symbols:
        characters += string.punctuation

    if not characters:
        return "Please try again. No character types selected."

    password_generated = ""
    for _ in range(Length):
        password_generated += random.choice(characters)

    return password_generated

def main():
    print("Hello ,Welcome to the Password Generator!")
    try:
        pass_length = int(input("Enter the length of the password you desire: "))
        use_letters = input("Include letters (enter y for yes/n for no)? ").lower() == 'y'
        use_numbers = input("Include numbers (enter y for yes/n for no)? ").lower() == 'y'
        use_symbols = input("Include symbols(enter y for yes/n for no)? ").lower() == 'y'
    except ValueError:
        print("Invalid input!, password length must be numeric values")
    

    generated_password = password_generator(pass_length, use_letters, use_numbers, use_symbols)

    print("Generated Password :", generated_password)

if __name__ == "__main__":
    main()
