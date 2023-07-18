from juego import Juego
from inventario import Inventario

def main():
    inventario = Inventario()
    juego = Juego(inventario)
    juego.iniciar_combate()

if __name__ == "__main__":
    main()


'''
En el mundo de Minecraft, se ha desatado una feroz batalla entre un valiente jugador y un poderoso monstruo. El jugador, llamado Steve, está equipado con un arma especial, mientras que el monstruo, un aterrador Creeper, se prepara para atacar.
El jugador tiene la capacidad de moverse en diferentes direcciones y usar una habilidad única para enfrentar a los enemigos. Por otro lado, el monstruo tiene la capacidad de rugir para aterrorizar a sus oponentes.
Durante el combate, tanto el jugador como el monstruo podrán atacar al oponente. Cada ataque reducirá los puntos de vida del objetivo. Además, las armas y habilidades especiales tendrán un poder adicional que se sumará al daño infligido.
Además de los puntos de vida, tanto el jugador como el monstruo tienen puntos y experiencia. Los puntos representan la puntuación acumulada por cada uno, mientras que la experiencia representa la progresión del jugador en el juego. Tanto los puntos como la experiencia pueden ser modificados por diferentes acciones, como derrotar a un enemigo o completar tareas especiales.
El objetivo del problema es simular un combate entre el jugador y el monstruo, teniendo en cuenta los modificadores de vida, puntos y experiencia. Deberás implementar las clases y métodos necesarios para llevar a cabo el combate, calcular el daño infligido por cada ataque y aplicar los modificadores correspondientes. Además, debes mostrar los mensajes de acción relevantes durante el combate, como movimientos, ataques y resultados de los enfrentamientos.

Recuerda tener en cuenta los conceptos de herencia, polimorfismo, encapsulamiento y abstracción en tu implementación.
las armas deben ser aleatroreas en cada inicio de programa, por ende cada arma tomara puntos de danhos diferentes, ademas que los niveles de xp de cada personaje al iniciar el combate tambien deben ser diferentes
la idea es que si bien no pedire que el combate sea manejado por una persona si debe ser dinamico y
divertido
puede que en un enfrentamiento gane Steve y en otro gane el Creeper
eso lo dira el nivel de cada personaje, el nivel de las armas y los pv que se le asignen a cada personaje
la idea es que si Steve gana pueda seguir peleando hasta con un maximo de 4 enemigos aleatorios
Hablas de movimiento
Steve en nivel 1 constara con 10 puntos de vida, el creeper constara con 8 pv
por ejemplo: en el primer turno steve ataca, el creeper tambien, siguiente movimiento el steve se mueve 2 cuadros y cambia a un arco, el creeper dependiendo del movimiento que tenga segun su nivel se puede mover o atacar o defenderse se entiende?
dare los stat bases de cada personaje, y las variaciones de los niveles. stev consta de 10 puntos de vida, 1 de movimiento, empieza con una espada de madera el creeper tiene 9 puntos de vida, 1 de movimiento y el grito por cada nivel steve sube 5 de vida y 1 de movimiento, cambiando la espada cada 2 niveles el enemigo cada nivele sube 3 puntos de vida y cada dos niveles sube 1 punto de movimiento la idea es que si yo empiezo el programa steve pueda aparecer con nivel 10 o con nivel 1, eso lo determinan con random, lo mismo aplica para el creeper.
solo por weviar, el nivel inicial no puede superar el nivel 5
Y si Steve ataca al Creeper el Creeper debe tener una posibilidad de explotar y quitarle vida a Steve depende si el programa elige eso
por cada muerte el personaje recibe experiencia, esta en el primer enemigo sera de 40 pto, para subir de nivel 1 a 2 se necesitan 30 pto de exp, por cada siguiente nivel la exp se multiplica por 2 de nivel 2 a 3 se necesitan 60 esto es para ambos casos
si el creeper gana este puede seguir peleando con mas enemigos siempre con un maximo de 3 humanos
Número de monstruos ilimitados y número de Steves 3
y lo mismo para el otro lado creeper, enemigo random 1, enemigo random 2
logicamente la idea es que todo eso se muestre enconsola de modo bonito
El humano en caso de que el monstruo lo mate, adquiera las stats del anterior?, gracias por la pregunta, recoge la expericia que suelta que es propocional al nivel del steve muerto.... PERO!!! no puede superar 2 niveles al creeper que esta atancando
segundo el creeper que queda vivo, recupera energia, igual que el steve
Si es así entonces subamos la cantidad de enemigos a 10 y con ordenamiento de inventario 🥳🥳
'''