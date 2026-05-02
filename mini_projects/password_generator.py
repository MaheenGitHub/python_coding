"""
genrate a password

ask user the number of letters, symbols ad numbers in the password

easy level -> unshuffled
difficult - shuffled

"""
import random

print("EWelcome to the pass word generator"
)

letter = int(input("How many letters do u want? "))
num = int(input("How many numbers do u want? "))
symbol = int(input("How many symbols do u want? "))

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "~!@#$%^&*()_+}{|\":<>?,./;'symbol[]\=-'\}"

print(letter , num, symbol )

password = ""
length = letter + num +symbol

for i in range(num) :
    password += str(random.randint(0,9))

for i in range(letter) :
    password += random.choice(alphabets)

for i in range(symbol):
    password += random.choice(symbols)


print(password)

print("Shuffled using shuffle(list)")
password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)