from juego import Juego
from inventario import Inventario

def main():
    inventario = Inventario()
    juego = Juego(inventario)
    juego.iniciar_combate()

if __name__ == "__main__":
    main()


'''
En el mundo de Minecraft, se ha desatado una feroz batalla entre un valiente jugador y un poderoso
monstruo. El jugador, llamado Steve, está equipado con un arma especial, mientras que el monstruo,
un aterrador Creeper, se prepara para atacar.

El jugador tiene la capacidad de moverse en diferentes direcciones y usar una habilidad única para
enfrentar a los enemigos. Por otro lado, el monstruo tiene la capacidad de rugir para aterrorizar a
sus oponentes.

Durante el combate, tanto el jugador como el monstruo podrán atacar al oponente. Cada ataque
reducirá los puntos de vida del objetivo. Además, las armas y habilidades especiales tendrán un
poder adicional que se sumará al daño infligido.

Además de los puntos de vida, tanto el jugador como el monstruo tienen puntos y experiencia. Los
puntos representan la puntuación acumulada por cada uno, mientras que la experiencia representa la
progresión del jugador en el juego. Tanto los puntos como la experiencia pueden ser modificados por
diferentes acciones, como derrotar a un enemigo o completar tareas especiales.

El objetivo del problema es simular un combate entre el jugador y el monstruo, teniendo en cuenta los 
modificadores de vida, puntos y experiencia. Deberás implementar las clases y métodos necesarios para 
llevar a cabo el combate, calcular el daño infligido por cada ataque y aplicar los modificadores 
correspondientes. Además, debes mostrar los mensajes de acción relevantes durante el combate, como
movimientos, ataques y resultados de los enfrentamientos.

Recuerda tener en cuenta los conceptos de herencia, polimorfismo, encapsulamiento y abstracción en tu 
implementación.
Un vez lo saque, nos quedamos con lo que hay
Ooh ya me vine
Puta justo estoy almorzando
las armas deben ser aleatroreas en cada inicio de programa, por ende cada arma tomara puntos de danhos
diferentes, ademas que los niveles de xp de cada personaje al iniciar el combate tambien deben ser
diferentes
Qué tan interactivo quieres que sea?
la idea es que si bien no pedire que el combate sea manejado por una persona si debe ser dinamico y
divertido
puede que en un enfrentamiento gane Steve y en otro gane el Creeper
eso lo dira el nivel de cada personaje, el nivel de las armas y los pv que se le asignen a cada personaje
la idea es que si Steve gana pueda seguir peleando hasta con un maximo de 4 enemigos aleatorios
Con cierto grado de aleatoriedad
exacto
Me gusta
Ni más preguntas por mi parte
Hablas de movimiento
Steve en nivel 1 constara con 10 puntos de vida, el creeper constara con 8 pv
Osea el daño y las armas tengo una idea de cómo hacerlo pero a qué te refieres con movimiento en diferentes
direcciones?
También mencionas sobre varios enemigos, está bien si Steve puede mandar a luchar a varios mini Stevens y
el mounstro Creeper a su vez mandar a varios mini Creepers
por ejemplo: en el primer turno steve ataca, el creeper tambien, siguiente movimiento el steve se mueve 2
cuadros ycambia a un arco, el creeper dependiendo del movimiento que tenga segun su nivel se puede mover o
atacar o defenderse
se entiende?
Claro
dare los stat bases de cada personaje, y las variaciones de los niveles.
Yo tampoco tengo más preguntas por ahora, me gusto mucho este ejercicio
stev consta de 10 puntos de vida, 1 de movimiento 1, empieza con una espada de madera
el creeper tiene 9 puntos de vida, 1 de movimiento y el grito
por cada nivel steve sube 5 de vida y 1 de movimiento, cambiando la espada cada 2 niveles
el enemigo cada nivele sube 3 puntos de vida y cada dos niveles sube 1 punto de movimiento
la idea es que si yo empiezo el programa steve pueda aparecer con nivel 10 o con nivel 1, eso lo determinan
con random
lo mismo aplica para el creeper
Mm, y puedo elegir entre atacar o moverme
solo por weviar, el nivel inicial no puede superar el nivel 5
ataque, defensa, movimiento
Y si Steve ataca al Creeper el Creeper debe tener una posibilidad de explotar y quitarle vida a Steve
depende si el programa elige eso
Entonces sería entre 1 y 5
entre 1 a 5
Perfecto
por cada muerte el personaje recibe experiencia, esta en el primer enemigo sera de 40 pto, para subir de
nivel 1 a 2 se necesitan 30 pto de exp, por cada siguiente nivel la exp se multiplica por 2
de nivel 2 a 3 se necesitan 60
esto es para ambos casos
Y que pasa si el personaje muere? Se reinicia los niveles de experiencia o se mantiene?
si el creeper gana este puede seguir peleando con mas enemigos siempre con un maximo de 3 humanos
se cierra el programa se inica de nuevo en aleatoreo
Yap
Pero estás diciendo que hay un máximo de 3 humanos?
Tendría que morirse los 3 humanos para que se cierre el programa
si steve mata al creeper debe continuar contra otro monstruo
asi mismo el creeper si mata a steve debe continuar contra otro humano
Número de monstruos ilimitados y número de Steves 3
y lo mismo para el otro lado creeper, enemigo random 1, enemigo random 2
quien muera primero gana
se entiende???
Claro
Lo único malo es q si solo hay tres monstruos no se va a poder acumular muchos puntos de nivel
Te wa pegar
da igual, quieres hacerlo eterno
Me callo, pregunta tu
genra minecraft completo en python
@Seba vives?
XD
lo tienen de esclavo
Murió después del primero texto
Yo ya cerré las preguntas mías
Mal ahí
Yap
de aqui al viernes creo que es tiempoo mas que suficiente para hacer esto
Aún me quedé con varias dudas
habla
Si se generan 3 tipos de Steves y 3 tipos de monstruos de manera aleatoria ilimitadamente
Cómo se acaba el juego?
Opción acabar juego?
piensalo como si fueran una linea de 3
o como pokemon
entra el primer steve y el primer creeper
muere steve 1 y entra steve 2
Claro
si steve 2 mata al creeper 1, entra el creeper 2
el primero que mate a los 3 perosnajes del contrincario gana
Claro eso lo entiendo
logicamente la idea es que todo eso se muestre enconsola de modo bonito
no sirve si ejecutas el programa y corre todo hasta abajo
Pero entonces el sistema de experiencia y de maxeado de armas, no se va a poder implementar, porque a lo
mucho que vas a llegar sería unos dos o 3 niveles más
Ya que solo puedes matar a 3 enemigos
pero eso es lo lindo con el segundo enemigo generas nivel y cambias arma
Ok ok, ahora sí me quedo todo claro
no puede ser la misma arma y el nivel varia dependiendo con el que partan
El humano en caso de que el monstruo lo mate, adquiera las stats del anterior?
gracias por la pregunta, recoge la expericia que suelta que es propocional al nivel del steve muerto....
PERO!!! no puede superar 2 niveles al creeper que esta atancando
segundo el creeper que queda vivo, recupera energia
igual que el steve
Que puto que no pueda superar dos niveles al Creeper jajajsj
Yap
piensa que el steve 2 puede llegar con mayor nivel a creeper 1 por ejemplo 7 contra 3... y ademas gana 
proporcinal al nivel del que perdio... eso quiere decir que si el primer steve perdio debe tener o nivel 1 
o 2
osea minimo 30 pto de exp a 60 ptos de ex
Osea del lvl1 al 3
Que con 60 de xp eres lvl 3
La cosa es q no puede superar de nivel al rival si muere
ahora bien, como nadie pregunto, la idea es que funcione de verdad como minecraft
es decir los steve tienen inventarios que pueden tener cosas que puedan curarse
Espacio de inventario para equipación
pero el de nivel 1 no puede tener las mismas cosas que el de nivel 3
De armadura
😐
Se van upgradeando
Pociones
Crafteos
Materiales XD
Tu lo vas a hacer también no?
nada de caras culiao, tu pediste que te sacara el jugo
quien???
quien yo???
Te lo hago en tkinder entonces po
No el @Seba digo
Se me hace más fácil si quieres inventario y todo
weon cada uno debe hacerlo por separado
poo solamente
y agradece que no meti ordenamiendo te inventario
Lo digo, pq el qliao encima te da más ideas 🤣
Ctmr 🤣🤣
Respuestas hasta las 5 y media @Seba
Respuesta de?
Yo me remito a lo que te digo Rodrigo
.
Yap, entones muchas gracias señor rodrigo
Una última cosa
Don misael la fecha de entrega cuando será?
Viernes quedamos no?
Daré más tiempo ya que el Sebastián no ha visto poo
Eso mismo estaba pensando
Daré 2 semanas
Shaa
Jajaja
Okey
El qlao 🤣
Osea dale
Tamos entonces
Si es así entonces subamos la cantidad de enemigos a 10 y con ordenamiento de inventario 🥳🥳
Por parte de steve
'''