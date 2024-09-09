#¿Como obtengo la cantida de palabras que tengo en mi cadena?
#palabras = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cum voluptatum animi aliquid accusantium magnam quam non similique laborum laudantium, odit harum labore nemo dignissimos ad asperiores officia nulla sequi dicta molestias itaque. Aliquid expedita magnam natus tenetur totam aliquam quae facere harum commodi cum, sequi incidunt, at atque ut aut"
#C= palabras.split()
#print(len(C))

#Si pido datos por un input voy a ver que tengo muchos parámetros que controlar, 
#como que lo que ingrese sea igual a lo que tenga en mi variable por ejemplo... 
#Como resuelvo para que me salga por terminal todo ok si quiero pasar por el input Micontrasenia
variableASeguir = "micontrasenia"
entrada = input("ingrese la contraseña: ")
if entrada == variableASeguir:
  print("todo ok")
else:
  print("Todo mal")