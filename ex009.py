import random
import string
def letra_aleatoria():
     return random.choices(string.ascii_uppercase)
letra = letra_aleatoria()
print(letra)
