from personaje import Jugador, Enemigo
from arma import Espada, Arco

class Juego:
    def __init__(self):
        self.jugador = Jugador("Steve", Espada())
        self.enemigos = self.generar_enemigos()

    def generar_enemigos(self):
        enemigos = []
        nombres = ["Creeper", "Skeleton", "Zombie", "Enderman", "Spider", "Witch", "Cave Spider", "Slime", "Guardian", "Ghast"]
        for i in range(10):
            enemigos.append(Enemigo(nombres[i], "Habilidad especial"))
        return enemigos

    def iniciar_combate(self):
        for enemigo in self.enemigos:
            while self.jugador.puntos_de_vida > 0 and enemigo.puntos_de_vida > 0:
                self.mostrar_turno()
                self.realizar_accion()
                self.actualizar_estado()
                print()  # Agregar separación entre turnos

            if self.jugador.puntos_de_vida <= 0:
                print(f"El {enemigo.nombre} ha ganado el combate.")
                break
            else:
                print(f"El jugador ha derrotado al {enemigo.nombre}.")

    def mostrar_turno(self):
        print(f"--- Turno ---")
        print("Jugador:")
        self.jugador.mostrar_estado()
        print("Enemigo:")
        # Mostrar estado del enemigo

    def realizar_accion(self):
        accion = self.obtener_accion()
        if accion == "1":
            self.jugador.atacar(self.enemigo)
        elif accion == "2":
            self.jugador.cambiar_arma(Arco())
        elif accion == "3":
            self.jugador.usar_habilidad_especial(self.enemigo)
        else:
            print("Acción inválida. Se omite el turno del jugador.")

    def obtener_accion(self):
        print("Acciones disponibles:")
        print("1. Atacar")
        print("2. Cambiar de arma")
        print("3. Usar habilidad especial")
        return input("Ingrese el número de la acción que desea realizar: ")

    def actualizar_estado(self):
        if self.jugador.puntos_de_vida > 0:
            # Lógica para ganar puntos y experiencia
            pass

        if self.enemigo.puntos_de_vida > 0:
            # Lógica para ganar puntos y experiencia
            pass
