class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

    def info(self):
        print("Olá, ", self.getNome())
