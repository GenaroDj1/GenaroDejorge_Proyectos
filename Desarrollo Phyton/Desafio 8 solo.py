import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ruta='/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio8/ExcelDesafio8.xlsx' 
#para usarlo aca hay que cambiar la ruta a ruta de archivos de la pc
df= pd.read_excel('/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio8/ExcelDesafio8.xlsx')
df

#grafio de torta con encuesta
platform_counts = df['¿Cual es la bebida caliente que tomas cotidianamente?'].value_counts() 
plt.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%')
plt.title('Bebida Caliente')
plt.show()

#grafio de barra con encuesta
sns.countplot(x='¿Qué tipo de música prefieres?', data=df)
plt.title('Tipo de musica')
plt.show()

#grafio de torta con encuesta
platform_counts = df['¿Cual es tu estacion del año favorita?'].value_counts()
plt.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%')
plt.title('Estaciones')
plt.show()

sns.countplot(x='¿Cuál es tu destino vacacional ideal?', data=df)
plt.title('Vacaciones')
plt.show()
