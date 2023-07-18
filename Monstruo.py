from personaje import Personaje


class Monstruo(Personaje):
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item):
        super().__init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item)        
        self.puntosDeVida = 9
        self.puntos = 100
        self.nivel = 1
        self.defensa = 1
        self.movimiento = 1

    def atacar(self):
        pass

    def recibirAtaque(self,danho):
        pass

    def mover(self):
        pass

    def habilidad(self):
        pass

    def cosnseguirXp(self, cantidad):
        pass

    def derrota(self):
        pass

    def loot():
        pass