from item import Item


class Armadura(Item):
    def __init__(self, tipo, defensa, durabilidad):
        self.tipo = tipo
        self.defensa = defensa
        self.durabilidad = durabilidad
    
    def critico():
        pass
