import pandas as pd
import matplotlib as plt

#Otra manera
def crear_grafico_puntos_interactivo():

    datos_usuario = input("Ingrese los datos separados por comas (ejemplo: 10,15,20,25,30): ")
    datos = [float(dato) for dato in datos_usuario.split(",")]

    nombre_grafico = input("Ingrese el nombre del gráfico: ")
    titulo = input("Ingrese el título del gráfico: ")
    nombre_eje_x = input("Ingrese el nombre del eje x: ")
    nombre_eje_y = input("Ingrese el nombre del eje y: ")

    plt.figure(figsize=(8, 6))
    plt.scatter(range(1, len(datos) + 1), datos) #scatter significa graf de puntos, barras es bar y lineas es plot

    plt.title(titulo)
    plt.xlabel(nombre_eje_x)
    plt.ylabel(nombre_eje_y)

    plt.savefig(f"{nombre_grafico}puntos.png")
    plt.show()

crear_grafico_puntos_interactivo()

def grafico_barras_interactivo():

    datos_usuario = input("Ingrese los datos separados por comas (ejemplo: 10,15,20,25,30): ")
    datos = [float(dato) for dato in datos_usuario.split(",")]

    nombre_grafico = input("Ingrese el nombre del gráfico: ")
    titulo = input("Ingrese el título del gráfico: ")
    nombre_eje_x = input("Ingrese el nombre del eje x: ")
    nombre_eje_y = input("Ingrese el nombre del eje y: ")

    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(datos) + 1), datos)

    plt.title(titulo)
    plt.xlabel(nombre_eje_x)
    plt.ylabel(nombre_eje_y)

    plt.savefig(f"{nombre_grafico}barras.png")
    plt.show()

grafico_barras_interactivo()

def grafico_Lineas_interactivo():

    datos_usuario = input("Ingrese los datos separados por comas (ejemplo: 10,15,20,25,30): ")
    datos = [float(dato) for dato in datos_usuario.split(",")]

    nombre_grafico = input("Ingrese el nombre del gráfico: ")
    titulo = input("Ingrese el título del gráfico: ")
    nombre_eje_x = input("Ingrese el nombre del eje x: ")
    nombre_eje_y = input("Ingrese el nombre del eje y: ")

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(datos) + 1), datos)

    plt.title(titulo)
    plt.xlabel(nombre_eje_x)
    plt.ylabel(nombre_eje_y)

    plt.savefig(f"{nombre_grafico}barras.png")
    plt.show()
grafico_Lineas_interactivo()