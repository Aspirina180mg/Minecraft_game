#Usan comillas simples o dobles, y no diferencian entre ellas, son case sensitive
a = 'comilla simple'
b = "comilla doble"
# se pueden crear strings multi linea al usar 3 comillas
c = '''texto
multi
linea'''

d = "pastel" # d es igual a f pero no son iguales a e
e = "Pastel"
f = 'pastel'

#No existen las variables de tipo char, son strings de largo 1, por lo que los strings son arrays.
print(d[3]) #imprimirá la letra t

#igualmente se pueden usar índices para imprimir parte de un texto
print(d[1:4])
#desde el índice 1 hasta el 4, sin incluirlo, imprime "ast¨

# se puede recortar desde el comienzo o desde el final
print(d[:5]) #Imprimirá "paste"
print(d[2:]) #imprimirá "stel!"

# tambien se puede usar índices negativos, por alguna razón
print(d[-3:-1]) #imprime "te"

#se puede circular un string con un ciclo for
for x in d:
	print (x) #imprime todas las letras de la palabra pastel, una por una

#se puede conocer el largo de un string con la funcion len()
print(len(d)) # imprime el número 6

#se puede usar "in" para chequear si una frase o letra ya está en un string
print ("te" in d) #imprime True, porque la palabra "te" existe dentro de pastel

#Funciones de modificación de Strings
d = " Delicioso pastel "
print(d.upper()) #TEXTO EN MAYUSCULAS
print(d.lower())  #texto en minúsculas
print(d.strip())  #eliminar espacio sobrante, sea al principio o al final
print(d.replace("pastel", "postre")) #reemplazar strings, en este caso imprime "Delicioso postre"
print(d.split(" "))  #separar strings, devuelve una lista con los elementos

#concatenación
g = "El alfajor"
print(g + " es un " + d.strip().lower())

#strings y números
print(f"{g} es un {d.strip().lower()}")