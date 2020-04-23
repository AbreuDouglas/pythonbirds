class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade +=1
    def frear(self):
        self.velocidade =0 if self.velocidade - 2 < 0 else self.velocidade -2

if __name__ == '__main__':
    # Testando Motor
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print( motor.velocidade)

class Direcao():
    def __init__(self):
        self.direcao = 'Norte'

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'

if __name__ == '__main__':
    # Testando Direcao
    direcao = Direcao()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)


from motor import Motor
from direcao import Direcao

class Carro():
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.direcao

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    print(carro.calcular_direcao())
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())