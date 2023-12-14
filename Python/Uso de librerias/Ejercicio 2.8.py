#Genera a partir de los datos de abajo un archivo excel y lo guarda en un dataframe
#datos = {
#    'Nombre': ['Juan', 'María', 'Carlos', 'Laura'],
#    'Edad': [25, 30, 22, 28],
#    'Ciudad': ['Buenos Aires', 'Madrid', 'Ciudad de México', 'Lima']
#}

# Crear un DataFrame
#df = pd.DataFrame(datos)

# Especificar el nombre del archivo Excel
#nombre_archivo = 'datos_ejemplo.xlsx'

# Guardar el DataFrame en un archivo Excel
#df.to_excel(nombre_archivo, index=False)

#print(f'Se ha creado el archivo Excel: {nombre_archivo}')
#----------------------------------------------------------------------------------------------------------------
#Ejercicio 2.8 hecho en collab
#from google.colab import drive
#drive.mount('/content/drive') #monta la conexion con el drive

#import sys
#sys.path.append('/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python') #importa la carpeta que seleccionemos de nuestro drive

#Importá la librería
#import numpy as np
#import pandas as pd

# Cargá el archivo CSV en un DataFrame
#from google.colab import files #permite importar codigos csv a google colab
#uploaded = files.upload()

# Reemplaza 'nombre_del_archivo.csv' con el nombre real de tu archivo CSV
#nombre_archivo = 'vgsales.csv'

# Cargar el archivo CSV en un DataFrame de Pandas
#df= pd.read_csv(nombre_archivo)

# Visualizar las primeras filas del DataFrame para asegurarte de que se haya cargado correctamente
#df.head()

#importá la librería para graficar matplotlib
#import matplotlib.pyplot as plt
# Filtrá los datos y generá un dataFrame con los juegos mas vendidos y sus nombres
#df_ordenado = df.sort_values(by='Global_Sales', ascending=False)
#df_ordenado

# Creá un gráfico de barras con los nombres de esos jugadores y los goles
#import matplotlib.pyplot as plt
#df.plot.scatter(x="Global_Sales", y= "Rank")
#plt.xlabel('Ranking')
#plt.ylabel('Ventas Globales')
#plt.title("Mejores videojuegos")
#plt.legend()
#plt.show()

#para graficar un dataframe primero tenés que poner algo así 
#nombre_dataframe.plot.scatter(x="nombre_columna", y="nombre_columna")