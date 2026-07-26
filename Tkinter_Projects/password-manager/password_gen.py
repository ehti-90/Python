import string
import random


# Lowercase alphabets
small_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Uppercase alphabets
capital_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Digits
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Common symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*'
]

letter = random.randint(2,6)
capital = random.randint(2,5)
digits = random.randint(1,3)
symbol = random.randint(3,5)


def generate():
    
    password =[random.choice(small_letters) for _ in range(letter)]
    password += [random.choice(capital_letters) for _ in range(capital)] # This will ad to prev not override it
    password += [random.choice(numbers) for _ in range(digits)]
    password += [random.choice(symbols) for _ in range(symbol)]


    password_1 =""

    random.shuffle(password) # shuffles the passwords char so its not predictable
    for i in password:
        password_1 += i
    
    return password_1




    


