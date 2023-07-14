import random

class Arma:
    def __init__(self, nombre, dano):
        self.nombre = nombre
        self.dano = dano

    def generar_dano(self):
        return self.dano

class Espada(Arma):
    def __init__(self):
        super().__init__("Espada de madera", random.randint(1, 5))

class Arco(Arma):
    def __init__(self):
        super().__init__("Arco", random.randint(3, 7))

# Otras subclases de Arma según los requisitos del juego
