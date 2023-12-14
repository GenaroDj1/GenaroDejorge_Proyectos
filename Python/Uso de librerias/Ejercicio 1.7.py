#A partir del siguiente diccionario:
#alumnos_curso = {'python': [35, 28, 61, 36, 25], 'DWI': [21, 52, 32, 25, 30], 'robotica': [25, 20, 41, 37, 22]}
#crear un dataframe que se vea como:
import pandas as pd
alumnos_curso = {'python': [35, 28, 61, 36, 25], 'DWI': [21, 52, 32, 25, 30], 'robotica': [25, 20, 41, 37, 22]}
df_alumnos= pd.DataFrame(alumnos_curso)
df_alumnos.index =["lunes", "martes", "miercoles", "jueves","viernes"]
print(df_alumnos)