from inventario import Inventario, Item, Arma, Armadura

# Crear un inventario
inventario = Inventario()

# Crear algunos items
item_pocion = Item("Poción de salud", 10, "Restaura vida")
espada_madera = Arma("Espada de madera", "Espada", 10, 100)
armadura_cota_malla = Armadura("Armadura de cota de malla", "Armadura", 5, 200)
item_llave = Item("Llave", 1, "Abre una puerta")
item_pocion2 = Item("Otra Poción de salud", 5, "Restaura vida")

# Agregar items al inventario
inventario.agregar_item(item_pocion)
inventario.agregar_item(espada_madera)
inventario.agregar_item(armadura_cota_malla)
inventario.agregar_item(item_llave)
inventario.agregar_item(item_pocion2)
inventario.agregar_item(espada_madera)

# Mostrar el inventario
inventario.mostrar_inventario()
