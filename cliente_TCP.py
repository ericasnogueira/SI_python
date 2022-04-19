#importando a biblioteca socket
import socket
# importanto sys == fornecendo o acesso a algumas var e funções com o interpretrador
import sys

# tentar uma conexao com tcp e ip
def main():
    try:
        #objeto de conexão
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e: # se der erro vai ser chamado de e
        print("A conexão deu falha !!!")
        print(f'Erro : {e}')#mostrar qual foi o erro
        sys.exit()# se der o erro ele irá sair do programa
    
    print('Socket criado com sucesso')


    #Definindo qual vai ser o Host
    HostAlvo = input('Digite o Host ou Ip a ser conectado : ')
    PortaAlvo = input("Digite a porta a ser conectada : ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host : ",HostAlvo , " e  na Porta : ", PortaAlvo)
        # para não gerar um loop de ficar se conectando 
        s.shutdown(2) # desligar depois de 2 segundos
    except socket.error as e :
        print('Não foi possível conectar no host : ', HostAlvo ," e na Porta : ", PortaAlvo)
        print(f'Erro : {e}')
        sys.exit()# se der o erro sair do programa


if __name__ == '__main__' :
    main()