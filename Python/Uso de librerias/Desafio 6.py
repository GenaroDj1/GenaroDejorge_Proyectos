import pandas as pd

# FUNCION 1
# Una función que reciba como parámetro un DataFrame y nos devuelva el promedio de una columna en específico.
df_equipos = pd.DataFrame({'Equipos': ['BocaJrs','River Plate','Estudiantes','Huracan'],
        'Posición' : [1,2,3,4],
        'Puntos' : [19,17,10,6]
        })

def calcular_promedio(df_equipos, nombreColumna):
    #resultado = (df_equipos['Puntos'].sum()) / 4
    resultado = (df_equipos[nombreColumna].mean())
    return resultado

#print('DataFrame:')
#print(df_equipos)
#print(f'La Suma de puntos de los Equipos da como Promedio: {calcular_promedio(df_equipos)}')

# FUNCION 2
# Una función que reciba una DataFrame y nos devuelva un diccionario con la cantidad de veces que se repite un valor.
def contar_repeticiones(dataframe, columna): #Uso de diccionario vacio donde se almacena el recuento 
    conteo = {}

    for valor in dataframe[columna]:
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1

    return conteo

Ejemplo= {'A': [1, 2, 2, 3, 3, 3]}
df = pd.DataFrame(Ejemplo)

resultado = contar_repeticiones(df, 'A')
print(resultado)
# FUNCION 3
# Una función que a todos las cadenas de caracteres que se tengan en el DataFrame, esten con todos sus caracteres en minuscula.
def convertir_a_minusculas(df):
    # Iterar sobre todas las columnas del DataFrame
    for columna in df.columns:
        # Verificar si la columna contiene cadenas de caracteres
        if df[columna].dtype == 'object':
            # Convertir todas las cadenas de caracteres a minúsculas
            df[columna] = df[columna].str.lower()

    return df

# Ejemplo de uso
data = {"apellido": ["ALVarez", "MARTINEZ", "Perez"], 'edad': [10, 78, 53]}
df = pd.DataFrame(data)

df_min = convertir_a_minusculas(df)
print(df_min)