import random
import string

def passgen():

    char= string.ascii_letters+string.punctuation+string.digits

    password= random.choices(char, k=6)

    for i in password:
        print(i, end='')
    # OR print("".join(password))
passgen()