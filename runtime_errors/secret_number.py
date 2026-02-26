from module import isdigit
from os import system
system("clear")

secret_number = 333

print("Autheticating user...")
pwd = input("What's the secret number? ") # User Input

print()         # Skip Line
if not isdigit(pwd):
    print("Get a load of this guy mistaking a wor for a number. try again.")
if int(pwd) == 333:  # Check authentication
    print("Success! Opening RESTRICTED APP...")

else:
    print("That's the wrong number.")

print()         # Skip Line