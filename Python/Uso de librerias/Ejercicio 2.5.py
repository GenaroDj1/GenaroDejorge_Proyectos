import random


lista = []
for i in range(10): #Cantidad de elementos a imprimir
    lista.append(random.randint(0, 10)) #hace aparecer 10 numeros por el range que sean aleatorios entre 0 y 10


print(lista)