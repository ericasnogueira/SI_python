import hashlib

arquivo1 = 'a.txt'

arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

# tem que botar o caminho completo
hash1.update(open(r"C:\Users\erica\Documents\py\SI PYTHON\comparadordehashes\a.txt", 'rb').read())
 
hash2 = hashlib.new('ripemd160')

hash2.update(open(r"C:\Users\erica\Documents\py\SI PYTHON\comparadordehashes\b.txt", 'rb').read())

#comparação entre si

if hash1.digest() != hash2.digest():
    print(f'O arquivo : {arquivo1} é diferente do arquivo : {arquivo2}')
    print('O hash do arquivo a.txt é : ', hash1.hexdigest())
    print('O hash do arquivo b.txt é : ', hash2.hexdigest())
else:
    print(f'O arquivo : {arquivo1} é igual ao arquivo : {arquivo2}')
    print('O hash do arquivo a.txt é : ', hash1.hexdigest())
    print('O hash do arquivo b.txt é : ', hash2.hexdigest())


