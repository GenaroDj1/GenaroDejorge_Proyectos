import pandas as pd
import numpy as np

# Crear un DataFrame con datos ficticios
#Ejemplo = pd.DataFrame({
#    'nombre': ['Ana', 'Juan', 'María', 'Carlos'],
#    'edad': [25, 30, 28, 22],
#    'puntaje': [85, 92, 78, 65]
#})

#Mi dataframe:
peliculas = pd.DataFrame({
    'Nombre': ["Boogeyman", "La monja 2", "El cadaver de la novia", "Slenderman"],
    'Directores': ["Rob Savage", "Michael Chaves", "Tim Burton-Mike Johnson", "Sylvain White"],
    'Años de produccion': [2023, 2023, 2005, 2018],
    'Duracion': ["1h 38m", "1h 50m", "1h 17m", "1h 40m" ]
})
#print(peliculas)

# Mostrá las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(peliculas.loc[0])

# Mostrá información básica del DataFrame
print("Información básica del DataFrame:")
print(peliculas.info())

# Calculá estadísticas descriptivas (describe)
print("Estadísticas descriptivas del DataFrame:")
print(peliculas.describe())

# Filtrá las filas basadas en una condición, (por ejemplo, que la edad sea menor a 25)
mayor_2010= peliculas[peliculas['Años de produccion'] > 2010] #filtra las peliculas que fueron producidas despues del 2010
print(mayor_2010)

# Ordená los datos por una columna en orden ascendente.
print(peliculas.sort_values('Años de produccion'))

# Agregamos una columna, en este caso doble_puntaje. Agregale la columna contrasenia que sea el nombre y la edad juntos. Ej: Ana25
peliculas["Años de produccion"] = [2023, 2023, 2005, 2015]
print(peliculas) 

# Mostrá los datos modificados
print("Datos filtrados:")
print(peliculas['Años de produccion'])

# Mostrá los datos ordenados
print("Datos ordenados:")
print(peliculas.sort_values('Años de produccion'))
