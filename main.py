import string
from random import choice

values = string.ascii_letters + string.digits + string.punctuation
length = 8
password = ''

for i in range(length):
    password += choice(values)

print(password)