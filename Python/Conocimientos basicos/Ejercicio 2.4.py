#Practicaremos las diferencias entre  el return y el print.
#¿Qué sucede con el mensaje dentro del último print? #no llega, el comando se corta antes ya que return lo devuelve
#¿Te animás a generar diferentes instrucciones antes y después del return? ¿Cuáles de ellas se ejecutan? #se ejecutan solo las que estan antes del return

def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
    
mi_funcion() # Entra en mi_funcion

#def saludo(nombre):
#    return "Hola " + nombre

#bienvenida = saludo("Martina")
#print(bienvenida)
