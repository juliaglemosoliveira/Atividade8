class Veiculo:
    def mover(self):
        print("O veículo está se movendo")

def mover_veiculo(veiculo):
    veiculo.mover()

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo")

class Aviao(Veiculo):
    def mover(self):
        print("O avião está voando")

# Função mover_veiculo() passando as instâncias das subclasses
mover_veiculo(Carro())
mover_veiculo(Aviao())
