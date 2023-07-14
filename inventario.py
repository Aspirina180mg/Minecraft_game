class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def mostrar_inventario(self):
        print("Inventario:")
        if self.items:
            for item in self.items:
                print(item)
        else:
            print("El inventario está vacío.")
