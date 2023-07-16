import random

class Personaje:
    def __init__(self, nombre, puntos_de_vida, movimiento, inventario):
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
        self.movimiento = movimiento
        self.nivel = random.randint(1, 5)
        self.puntos = 0
        self.experiencia = 0
        self.inventario = inventario

    def atacar(self, objetivo):
        pass

    def recibir_dano(self, dano):
        pass

    def ganar_puntos(self, puntos):
        self.puntos += puntos

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia

    def mostrar_estado(self):
        pass

class Humano(Personaje):
    def __init__(self, nombre, inventario):
        super().__init__(nombre, 10, 1, inventario)

    def usar_habilidad_especial(self, enemigo):
        print(f"{self.nombre} usa su habilidad especial contra {enemigo.nombre}.")
        # Implementar lógica de habilidad especial

class Monstruo(Personaje):
    def __init__(self, nombre, inventario):
        super().__init__(nombre, 9, 1, inventario)

    def usar_habilidad_especial(self, jugador):
        print(f"{self.nombre} usa su habilidad especial contra {jugador.nombre}.")
        # Implementar lógica de habilidad especial
