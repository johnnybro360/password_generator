import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
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

print("Generated password:", generate_password(length))