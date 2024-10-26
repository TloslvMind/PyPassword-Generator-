from string import ascii_letters, digits, punctuation
from random import choices, shuffle

password = []

print("Welcome to the PyPassword Generator!")

amount_letter = int(input("How many letters would you like in your password?\n"))
amount_symbols = int(input("How many symbols would you like?\n"))
amount_numbers = int(input("How many numbers would you like?\n"))

password.extend(choices(ascii_letters, k=amount_letter))
password.extend(choices(digits, k=amount_symbols))
password.extend(choices(punctuation, k=amount_numbers))

shuffle(password)

print(f"Here's your password:   {''.join(password)}")