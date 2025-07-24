import random
import string

while True:
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)

    again = input("Do you want to generate another password? (y/n): ").lower()
    if again != 'y':
        print("Goodbye people!")
        break
