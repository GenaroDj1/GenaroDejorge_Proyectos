#Creá manualmente un archivo .txt. La primera línea colocarás tu mail de gmail. 
#En la segunda línea la contraseña obtenida para utilizar en Python.
#Guarda el archivo como credenciales.txt. 
#Luego lee el archivo con Python y a partir de lo leído creá dos variables: mail y contraseña.
#Notarás que en el mail aparecerá el caracter especial \n. Puedes eliminarlo con las siguientes líneas:

#cadena="sabrina.sanches@bue.edu.ar\n"
#corte= cadena.find("\n")
#mail= cadena[0:corte]

#El comando cadena.find(“\n”) encuentra el índice de \n en la cadena. 
#Luego indicamos que de la cadena se tome la subcadena desde el índice 0 hasta el que nos devolvió el método find (corte).
#Imprime el mail y contraseña para verificar que coincide con el .txt.

import yagmail 

Ruta = "/content/drive/MyDrive/Curso_python_Lonely"
Credenciales = "/content/drive/MyDrive/Curso_python_Lonely/Credenciales.txt"

# Abre el archivo en modo lectura ('r')
with open(Credenciales, 'r') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()

# Imprime cada línea del contenido leído
for linea in lineas:
    print(linea.strip())  # strip() elimina los espacios en blanco alrededor de cada línea


# Abre el archivo en modo lectura ('r')
with open(Credenciales, 'r') as archivo:
    # Lee la primera línea y la almacena en la variable primera_linea
    primera_linea = archivo.readline().strip()

    # Lee la segunda línea y la almacena en la variable segunda_linea
    segunda_linea = archivo.readline().strip()

# Imprime las variables
print("Primera línea:", primera_linea)
print("Segunda línea:", segunda_linea)