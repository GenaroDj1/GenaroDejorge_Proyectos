#Codigo hecho con mis compañeros de curso de desarrollo en python, donde se utilizo google drive con archivos 
#con google colab, separados entre "funciones" (Donde se creaba el codigo) y "Pruebas" archivo donde los tester 
#podian probar el codigo, grupo de 5 personas total.

#Link del drive: https://drive.google.com/drive/folders/1tczGsMYnGtYmTE4CseAMjY_6suQLuudc

#ver todos los modulos instalados de python
#pip list

#PARTE DE PROGRAMACION
import pandas as pd
#import numpy as np
from datetime import datetime

def contar_valor(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

def contar_cadena(lista, cadena):
    contador = 0
    for elemento in lista:
        if elemento == cadena:
            contador += 1
    return contador

# Función para calcular la edad dada la fecha de nacimiento
def calcular_edad(dia_nacimiento, mes_nacimiento, año_nacimiento):
    fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad


#PARTE DE TESTEO
# Ejemplo de uso contar valor
mi_lista = [1, 2, 3, 4, 2, 5, 2, 6, 2]
valor_a_contar = 2
resultado = contar_valor(mi_lista, valor_a_contar)
print(f"El valor {valor_a_contar} se repite {resultado} veces en la lista.")

# Ejemplo de uso contar cadena
mi_lista = ["manzana", "pera", "manzana", "naranja", "manzana", "uva", "manzana"]
cadena_a_contar = "manzana"
resultado = contar_cadena(mi_lista, cadena_a_contar)
print(f"La cadena '{cadena_a_contar}' se repite {resultado} veces en la lista.")

# Solicitar al usuario ingresar la fecha de nacimiento
dia_nacimiento = 3
mes_nacimiento = 6
año_nacimiento = 1989

# Validaciones pendientes
# Ceros en los dias o meses da error
# Poner meses mayores a 12 sino da error
# Poner fechas futuras da 0

# Llamar a la función para calcular la edad
edad = calcular_edad(dia_nacimiento, mes_nacimiento, año_nacimiento)
print(f"La edad es {edad} años.")