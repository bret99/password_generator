import random
import sys

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
special_symbols = "!@#$%&amp;*"
password = ""

try:
    length = int(input("Enter Password length: "))
    if int(length) < 8:
        sys.exit("\033[1;91mPassword length should be more than 8 characters!\033[1;00m")

    for i in range(int(length/3)):
        password += random.choice(letters)
        password += random.choice(digits)
        password += random.choice(special_symbols)
        if password.__len__() < 8:
            password += random.choice(letters)

    print(password)

except ValueError:
    sys.exit("\033[1;91mWrong input!\033[;00m")
