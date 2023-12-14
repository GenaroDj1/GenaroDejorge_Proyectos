#Vamos a jugar con los DataFrame y las Series para entender un poco mas como se manejan en Pandas estos tipos de datos.
#Importamos pandas y llamamos df a la variable que contenga a nuestro DataFrame. Este DataFrame tiene que tener 5 columnas y 4 filas
import pandas as pd
import numpy as np

# Generamos números aleatorios entre -100 y 100
data = np.random.randint(-100, 101, size=(4, 5))

# Creo el DataFRame
df = pd.DataFrame(data, columns=['Columna1', 'Columna2', 'Columna3', 'Columna4', 'Columna5'])
print(df)

#Realiza la suma de todos los elementos del Dataframe
df.sum()
print(f"Sumatoria total de todos los datos aleatorios del dataframe",(df.sum()).sum()) #sumatoria total de las colums

#print(df.sum()) #sumatoria de cada columna individual

#Imprimí el mínimo y el máximo del DataFrame:
df.min()
print(df.min()) #minimo de cada columna

print((df.min()).min()) #minimo del dataframe
#lo mismo pasa con el maximo:
df.max()
print(df.max())

#tambien se pueden imprimir a la vez:
print(df.min()).min(), print(df.max()).max()

#Teniendo en cuenta el siguiente dataFrame, 
#vamos a generar una función que multiplique esos valores por 0.8 para obtener el 80% de todos esos datos.

data = pd.DataFrame([[1000,2000,2300,4000,30000,250,12200],[1350,40700,3000,5000,45000,1250,1880],[1555,2340,2300,7000,300,3330,5022],[1356.50,200,130,8000,5550,21120,1876]],columns=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado','Domingo'])
print(data)

#crea un numero aleatorio del 0 al 100 y lo pasa como porcentaje multiplicando todo el dataframe
data2= np.random.randint(0, 100)
porcentaje= data2/100
print(data*porcentaje)

#Se le ingresa un numero entero que se convierte y se multiplica por todos los valores del dataframe
data2= int(input("ingrese un numero entero que sera el porcentaje que se use en el dataframe: "))
porcentaje= data2/100
print(data*porcentaje)