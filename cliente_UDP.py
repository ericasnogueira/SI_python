import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#SE FOR CRIADO COM SUCESSO
print('Cliente Socket criado com sucesso')

host = 'localhost'
porta = 5435 #porta que ele vai se conectar com o servidor
mensagem = 'OLÁ servidor '

try:
    print('Cliente : ', mensagem)
    s.sendto(mensagem.encode(), (host, 5434))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente : ' + dados)
finally:
    #fechando a conexão
    print('Cliente : fechando a conexão')
    s.close()
