
import string
import random
chars = string.ascii_letters+string.digits
chars = random.sample(chars,16)
chars = "".join(chars)
print(chars)
print(chars[3:5])