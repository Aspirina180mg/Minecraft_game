#import item
class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        if isinstance(item, Arma) or isinstance(item, Armadura):
            self.reemplazar_item(item)
        else:
            self.actualizar_cantidad(item)
        self.items.append(item)

    def reemplazar_item(self, nuevo_item):
        for i, item in enumerate(self.items):
            if isinstance(item, type(nuevo_item)):
                self.items[i] = nuevo_item
                break

    def actualizar_cantidad(self, item):
        for i, inv_item in enumerate(self.items):
            if isinstance(inv_item, type(item)):
                inv_item.cantidad += item.cantidad
                if inv_item.cantidad > 64:
                    inv_item.cantidad = 64
                break

    def mostrar_inventario(self):
        for item in self.items:
            print(f"{item.nombre}: Cantidad={item.cantidad}")


class Item:
    def __init__(self, nombre, cantidad, efecto):
        self.nombre = nombre
        self.cantidad = cantidad
        self.efecto = efecto

    def usar(self):
        pass


class Arma(Item):
    def __init__(self, nombre, tipo, ataque, durabilidad):
        super().__init__(nombre, 1, None)  # Se establece cantidad=1 para armas
        self.tipo = tipo
        self.ataque = ataque
        self.durabilidad = durabilidad

    def critico(self):
        pass

    def ataque(self):
        pass


class Armadura(Item):
    def __init__(self, nombre, tipo, defensa, durabilidad):
        super().__init__(nombre, 1, None)  # Se establece cantidad=1 para armaduras
        self.tipo = tipo
        self.defensa = defensa
        self.durabilidad = durabilidad

    def critico(self):
        pass