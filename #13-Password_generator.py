import random
import string

def generate_password(min_length,numbers=True,special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if(numbers):
        characters+=digits
    if(special_char):
        characters+=special

    pwd = ""
    meets_criteria = False  
    has_numbers=False
    has_special=False  

    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        if new_char not in letters and len(pwd)<1:
            continue
        pwd+=new_char

        if new_char in digits:
            has_numbers=True
        if new_char in special:
            has_special=True
        
        meets_criteria=True

        if numbers:
            meets_criteria=has_numbers
        if special_char:
            meets_criteria=meets_criteria and has_special
    return pwd

while True:
    min_length = int(input("Enter the length (8 or more): "))
    if not min_length < 8:
        break
    else:
        print("Try again")

has_numbers = input("Do u want numbers in it (y/n): ").lower() =="y"
has_special = input("Do u want special characters in it (y/n): ").lower() =="y"

pwd=generate_password(min_length,has_numbers,has_special)
print(f"The generated password is {pwd}")
