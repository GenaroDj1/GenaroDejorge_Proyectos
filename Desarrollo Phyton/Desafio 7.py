import matplotlib.pyplot as plt
import pandas as pd
#todo sacado del colab de hernan
# Crear un gráfico de barras para representar la popularidad de los lenguajes de programación
def generar_grafico_barras(df):
  plt.figure(figsize=(10, 6))
  plt.bar(df['Lenguaje de Programación'], df['Popularidad'], color='skyblue')
  plt.title('Popularidad de Lenguajes de Programación')
  plt.xlabel('Lenguaje de Programación')
  plt.ylabel('Popularidad')

  # Añadir etiquetas a las barras
  for i, v in enumerate(df['Popularidad']):
      plt.text(i, v + 2, str(v), ha='center', va='bottom')

  # Mostrar el gráfico
  plt.xticks(rotation=45)
  plt.tight_layout()
  # plt.show()
  return plt

# Crear un gráfico de líneas para representar la popularidad de los lenguajes de programación
def generar_grafico_lineas(df):
  plt.figure(figsize=(10, 6)) #significa que la figura tendrá un ancho de 10 pulgadas y una altura de 6 pulgadas.
  plt.plot(df['Lenguaje de Programación'], df['Popularidad'], marker='o', linestyle='-')
  plt.title('Popularidad de Lenguajes de Programación')
  plt.xlabel('Lenguaje de Programación')
  plt.ylabel('Popularidad')

  # Mostrar el gráfico
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.grid(True, linestyle='--', alpha=0.7)
  # plt.show()
  return plt

# Crear un gráfico de puntos para representar la popularidad de los lenguajes de programación
def generar_grafico_puntos(df):
  plt.figure(figsize=(10, 6))
  plt.scatter(df['Lenguaje de Programación'], df['Popularidad'], s=100, c='red', marker='o')
  plt.title('Popularidad de Lenguajes de Programación')
  plt.xlabel('Lenguaje de Programación')
  plt.ylabel('Popularidad')

  # Mostrar el gráfico
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.grid(True, linestyle='--', alpha=0.7)
  # plt.show()
  return plt

# Crear un DataFrame con datos de programación
data = {
    'Lenguaje de Programación': ['Python', 'Java', 'JavaScript', 'C++', 'Ruby'],
    'Popularidad': [80, 65, 70, 45, 30],
}

df = pd.DataFrame(data)

