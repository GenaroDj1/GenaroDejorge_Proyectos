# Importamos las librerías necesarias. Numpy la usamos si queremos crear mas funciones
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = "/content/jugadores_selección.xlsx"
jugadores = pd.read_excel(path)
print(jugadores)
#En este caso creo una variable llamada promedio.
# Intentá crear tu función para ejecutarla en la variable.
promEdad= sum(jugadores["EDAD"])/len(jugadores["EDAD"])

# Un clásico filtro dentro de la variable jugadores.abs
maschicos = jugadores[jugadores['EDAD']<=promEdad]
masgrandes = jugadores[jugadores['EDAD']>=promEdad]
#¿Que otras cosas se te ocurren que podemos buscar para guardar?
#Altura, peso, regate, etc.
# Selecciónamos el nombre y la edad en cada una de esas variables
xc = maschicos["NOMBRE"]
yc = maschicos["EDAD"]
xg = masgrandes["NOMBRE"]
yg = masgrandes["EDAD"]

# Genero el gráfico que quiero y le agrego su descripción
plt.axhline(y=promEdad, color='r', label="promedio")
plt.scatter(xc, yc, label="mas chicos")
plt.scatter(xg,yg, label="mas grandes")

plt.xlabel('NOMBRE')
plt.ylabel('Edad')
# genero una grilla que en este caso me sirve par aidentificar los valroes de los puntos del eje x
plt.grid()
# Cambio los valores de los labels del eje x para que sea cada nombre y rotado 90° para que quede vertical.
plt.xticks(np.arange(len(jugadores["NOMBRE"])), jugadores["NOMBRE"], rotation='vertical')

plt.legend() # Muestro los label que le agregué a cada elemento
plt.show()

#probá graficar la posición en función de la edad de los jugadores.
plt.axhline(y=promEdad, color='r', label="promedio")
plt.scatter(xc, yc, label="mas chicos")
plt.scatter(xg,yg, label="mas grandes")

plt.xlabel('Posicion')
plt.ylabel('Edad')
plt.grid()
plt.xticks(np.arange(len(jugadores["Posicion"])), jugadores["Posicion"], rotation='vertical')

plt.legend() # Muestro los label que le agregué a cada elemento
plt.show()

#Graficá los goles (G) que convirtieron los defensores (POS = D) por un lado, y los goles que convirtieron los delanteros (POS = A).
plt.axhline(y=Goles, color='r', label="Goles")
plt.bar(xc, yc, label="Defensores")
plt.bar(xg,yg, label="Delanteros")

plt.xlabel('Defensores')
plt.xlabel('Delanteros')
plt.ylabel('Goles')
plt.grid()

plt.show()