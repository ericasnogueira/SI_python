import random
import string

tamanho = 16
#vai recerbe a estrutua da senha gerada
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.:;?/'


rnd = random.SystemRandom() 

print(''.join(rnd.choice(chars) for i in range(tamanho)))