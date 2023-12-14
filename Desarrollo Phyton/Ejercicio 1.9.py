#Vamos a crear un archivo .txt desde una lista. 
#En primer lugar debés crear una lista cuyos elementos sean cadenas 
#(pueden hacer una lista de tus artistas o canciones favoritas). 
#Luego queremos que esa lista quede guardada en un archivo .txt. 
#Utiliza lo que vimos en clase para crear el archivo, cada elemento debe quedar en líneas separadas, 
#uno debajo del otro. 

import yagmail 

archivo= "texto.txt"
artistas_mundiales= ["Beyoncé","Ed Sheeran","BTS",
            "Leonardo DiCaprio","Scarlett Johansson","Zhang Yimou","Banksy",
            "Yayoi Kusama","Jeff Koons","Haruki Murakami",
            "Chimamanda Ngozi Adichie","J.K. Rowling",
            "Shakira","Bad Bunny","Carlos Vives"]

with open(archivo, 'w+') as f: 
  for e in artistas_mundiales: 
    f.write(e) 
    f.write("\n")
    print(e)


