class Personaje:
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item):
        self.nombre = nombre
        self.puntosDeVida = puntosDeVida
        self.puntos = puntos
        self.experiencia = experiencia
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.movimiento = movimiento
        self.arma = arma
        self.armadura = armadura
        self.item = item

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