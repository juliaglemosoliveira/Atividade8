class Animal:
    def emitir_som(self):
        print("Som do animal")

def emitir_som(animal):
    animal.emitir_som()

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")


# Método emitir_som() da classe Animal
emitir_som(Animal())
# Método emitir_som() da classe Cachorro
emitir_som(Cachorro())
# Método emitir_som() da classe Gato
emitir_som(Gato())
