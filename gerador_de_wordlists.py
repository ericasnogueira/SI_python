
import itertools
import string


string = input('Palavra a ser permutada : ')


resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(' '.join(i))