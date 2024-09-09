Top_MejoresVideojuegos=["God of war", "Call of duty", "League of legends", "Crash bandicoot",
                         "Grand theft auto","Valorant","Minecraft","Mario Bros", "Picmin","Dota","Diablo"]
Escalar=["Primer", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto", "Septimo", "Octavo", "Noveno", "Decimo", "Onceavo"]
#Variables en minuscula!!
for i in range(len(Top_MejoresVideojuegos)):
   print (f"El {Escalar[i]} juego del top es, {Top_MejoresVideojuegos[i]}")
#Otra manera de hacerlo es usando el for y el index de la siguiente manera:
#for index, i in enumerate(Top_MejoresVideojuegos):
#        print("aparicion" o {Escalar[i]}, index, ':', i)
x=0
while (x<11):
    print (f"El {Escalar[x]} juego del top es, {Top_MejoresVideojuegos[x]}")
    x+=1