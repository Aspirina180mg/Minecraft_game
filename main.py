from juego import Juego
from inventario import Inventario

def main():
    inventario = Inventario()
    juego = Juego(inventario)
    juego.iniciar_combate()

if __name__ == "__main__":
    main()
