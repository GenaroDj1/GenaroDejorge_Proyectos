import pandas as pd
import matplotlib.pyplot as plt

#Mismo grafico pero sin exactitud de alumnos por dia:
alumnos_curso = {'python': [35, 28, 61, 36, 25], 'DWI': [21, 52, 32, 25, 30], 'robotica': [25, 20, 41, 37, 22]}
df_alumnos = pd.DataFrame(alumnos_curso)
df_alumnos.index = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Crear un gráfico de barras apiladas
ax = df_alumnos.plot(kind='bar', stacked=True, figsize=(10, 6))

# Personalizar el gráfico
plt.xlabel('Días de la semana')
plt.ylabel('Cantidad de Alumnos')
plt.title('Total de Alumnos por Día')
plt.legend(title='Curso', loc='upper left')

# Mostrar el gráfico
plt.show()


#Muestra la cantidad exacta de alumnos en cada dia de la semana:
alumnos_curso = {'python': [35, 28, 61, 36, 25], 'DWI': [21, 52, 32, 25, 30], 'robotica': [25, 20, 41, 37, 22]}
df_alumnos = pd.DataFrame(alumnos_curso)
df_alumnos.index = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# Crear un gráfico de barras apiladas
ax = df_alumnos.plot(kind='bar', stacked=True, figsize=(10, 6))

# Personalizar el gráfico
plt.xlabel('Días de la semana')
plt.ylabel('Cantidad de Alumnos')
plt.title('Total de Alumnos por Día')
plt.legend(title='Curso', loc='upper left')

# Agregar etiquetas con los valores exactos en las barras
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.annotate(f'{height}', (x + width / 2, y + height), ha='center')

# Mostrar el gráfico
plt.show()


plt.legend()

# Mostrar el gráfico
plt.show()