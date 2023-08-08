class Personaje:  # ? clase principal
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, 
                 ataque, defensa, movimiento, arma, armadura, item):
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

#Este es un comentario


    def atacar(self): pass

    def recibirAtaque(self, danho):
        pass

    def mover(self):
        pass

    def habilidad(self):
        pass

    def cosnseguirXp(self, cantidad):
        pass

    def derrota(self):
        pass


class Humano(Personaje):  # ? clase hija
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel, ataque, defensa, movimiento, arma, armadura, item):
        super().__init__(self, nombre, puntosDeVida, puntos, experiencia,
                         nivel, ataque, defensa, movimiento, arma, armadura, item)
        self.puntosDeVida = 10
        self.experiencia = 0
        self.nivel = 1
        self.ataque = self.nivel
        self.movimiento = 1

    def atacar(self):
        pass

    def recibirAtaque(self, danho):
        pass

    def mover(self):
        pass

    def habilidad(self):
        pass

    def cosnseguirXp(self, cantidad):
        pass

    def derrota(self):
        pass


#? Peer Review - no se hizo cambio por ser poco práctico y no aportar optimización


class Monstruo(Personaje):  # ? clase hija
    def __init__(self, nombre, puntosDeVida, puntos, experiencia, nivel,
                 ataque, defensa, movimiento, arma, armadura, item):
        super().__init__(self, nombre, puntosDeVida, puntos, experiencia,
                         nivel, ataque, defensa, movimiento, arma, armadura,
                         item)
        self.puntosDeVida = 9
        self.puntos = 100
        self.nivel = 1
        self.defensa = 1
        self.movimiento = 1


    def atacar(self):
        pass

    def recibirAtaque(self, danho):
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
