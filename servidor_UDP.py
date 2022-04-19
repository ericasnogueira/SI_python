
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso ')

host = 'localhost'
porta = 5434
#fazendo a ligação do cliente e servidor com o host e porta
s.bind((host, porta))
mensagem = 'Servidor : Olá cliente'

while 1 :
    dados, end = s.recvfrom(4096)

    if dados:
        print('servidor enviando mensagem ....')
        s.sendto(dados + (mensagem.encode()), end) 