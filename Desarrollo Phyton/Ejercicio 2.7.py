#Con el dataframe del ejercicio anterior hacer un gráfico de barras para cada uno de los cursos. En el eje x deben aparecer los días y el el y, la cantidad de alumnos/as.
#Si queremos guardar cada gráfico, utilizaremos la línea:
#plt.savefig("nombre_grafico.jpg")
#Luego de las líneas que generan el gráfico.
#Pondremos el nombre que queremos que tenga nuestro gráfico con su extensión (.jpg, .png).
#No dudes en preguntar con tus compañeros, compañeras y docentes cualquier duda que tengas al respecto. 
import pandas as pd
import matplotlib.pyplot as plt

alumnos_curso = {'python': [35, 28, 61, 36, 25], 'DWI': [21, 52, 32, 25, 30], 'robotica': [25, 20, 41, 37, 22]}
df_alumnos = pd.DataFrame(alumnos_curso)
df_alumnos.index = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Transponer el DataFrame para tener cursos en el eje x
df_alumnos = df_alumnos.T

# Crear gráfico de barras para cada curso
for curso in df_alumnos.index:
    plt.bar(df_alumnos.columns, df_alumnos.loc[curso], label=curso)

# Añadir etiquetas y leyenda
plt.xlabel('Días de la semana')
plt.ylabel('Cantidad de Alumnos')
plt.title('Cantidad de Alumnos por Curso')
plt.legend()

# Mostrar el gráfico
plt.show()