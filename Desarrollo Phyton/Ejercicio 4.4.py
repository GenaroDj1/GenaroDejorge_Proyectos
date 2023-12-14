#Creá una función que no reciba parámetros, 
#sino que te pida por un input nombres separados por coma y que luego devolverlas en formato capitalizado.

def obtener_nombres_capitalizados():
    entrada = input("Ingresa nombres separados por coma: ")
    nombres = entrada.split(',')  # Dividir la entrada en nombres usando la coma como separador
    nombres_capitalizados = [nombre.strip().capitalize() for nombre in nombres]  # Capitalizar y eliminar espacios en blanco
    return nombres_capitalizados

# Llamamos a la función y almacenamos el resultado
nombres_capitalizados = obtener_nombres_capitalizados()

# Imprimimos los nombres capitalizados
print("Nombres en formato capitalizado:", ", ".join(nombres_capitalizados))