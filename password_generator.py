import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter the password length (1-50): "))
        if length > 0 and length <= 50:
            break
        else:
            print("Invalid length. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

use_upper = False
use_lower = False
use_digits = False
use_special = False

if input("Include uppercase letters (A..Z)? (y/n)").lower() == "y":
    use_upper = True
if input("Include lowercase letters (a..z)? (y/n)").lower() == "y":
    use_lower = True
if input("Include digits (0..9)? (y/n)").lower() == "y":
    use_digits = True
if input("Include special characters (!@#$)? (y/n)").lower() == "y":
    use_special = True

if not use_upper and not use_lower and not use_digits and not use_special:
    print("No character type selected. Exiting.")
    exit()

print("Generated password:", generate_password(length, use_upper, use_lower, use_digits, use_special))
