i = 1
while i < 6: #imprime el valor de i mientras sea menor que 6
    if i <= 0:
        break  #cierra el ciclo si i es menor o igual a 0 para evitar errores
    if i == 2:
        i += 1
        continue  #salta a la siguiente iteración sin imprimir el valor
    print(i)
    i += 1
else:
    print("i ya no es menor que 6")  #Se ejecuta cuando la condición del ciclo es falsa