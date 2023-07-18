class Humano(Personale):
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item):
        super().__init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item)        
        self.puntosDeVida = 10
        self.experiencia = 0
        self.nivel = 1
        self.ataque = self.nivel
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