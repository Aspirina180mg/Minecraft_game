class Item: #?clase principal
    def __init__(self, nombre, cantidad, efecto):
        self.nombre = nombre
        self.cantidad = cantidad
        self.efecto = efecto
    
    def usar():
        pass

class Arma(Item):   #? clase hija
    def __init__(self, nombre, tipo, ataque, durabilidad):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.durabilidad = durabilidad
    
    def critico():
        pass

    def ataque():
        pass

class Armadura(Item):   #? clase hija
    def __init__(self, nombre, tipo, defensa, durabilidad):
        self.nombre = nombre
        self.tipo = tipo
        self.defensa = defensa
        self.durabilidad = durabilidad
    
    def critico():
        pass