import random

class Personaje:
    def __init__(self, nombre, puntos_de_vida, movimiento):
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
        self.movimiento = movimiento
        self.nivel = random.randint(1, 5)
        self.puntos = 0
        self.experiencia = 0

    def atacar(self, objetivo):
        pass  # Implementar lógica de ataque

    def recibir_dano(self, dano):
        pass  # Implementar lógica de recibir daño

    def ganar_puntos(self, puntos):
        self.puntos += puntos

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia

    def mostrar_estado(self):
        pass  # Implementar método para mostrar el estado del personaje

class Jugador(Personaje):
    def __init__(self, nombre, arma):
        super().__init__(nombre, 10, 1)
        self.arma = arma

    def cambiar_arma(self, nueva_arma):
        self.arma = nueva_arma

    def usar_habilidad_especial(self, enemigo):
        pass  # Implementar lógica de habilidad especial

class Enemigo(Personaje):
    def __init__(self, nombre, habilidad_especial):
        super().__init__(nombre, 8, 1)
        self.habilidad_especial = habilidad_especial
