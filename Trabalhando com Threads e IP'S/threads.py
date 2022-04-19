from threading import Thread
import time

def carro(velocidade, piloto):
    #onde o carro ira começar
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto {piloto} km : {trajeto} \n')



"""
def carro2 (velocidade):
    trajeto = 0 
    while trajeto <= 100 :
        print(f'Carro2 : {trajeto}')
        trajeto += velocidade
"""
t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[2, 'Python'])

t_carro1.start()
t_carro2.start()


"""

carro1(10)
carro2(20)
"""
