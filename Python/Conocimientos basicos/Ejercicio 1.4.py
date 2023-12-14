#Vamos a generar una función que le pasemos como parámetro un nombre y un apellido, 
#y la salida sea un saludo de bienvenida al nombre y apellido pasados como parámetros.

#def saludarA(nombre, apellido):
# print(f"Bienvenidx, {nombre} {apellido}, un placer conocerlx")  
#nombre= input("Ingrese su nombre:")
#apellido= input("Ingrese su apellido:")
#saludarA(nombre, apellido)

#Esta función tiene que recibir como parámetro una contraseña y 
#nosotros tenemos que evaluar si es segura o no, asegurandonos de que tenga:
#Al menos 8 caracteres
#Al menos un numero
def verificar_contraseña(contraseña):
    if 'ñ' in contraseña:
        return "La contraseña no puede contener la letra 'ñ'."
    if ' ' in contraseña:
        return "La contraseña no puede contener espacios."
    if len(contraseña) > 8:
        return "La contraseña no puede tener más de 8 caracteres."
    if len(contraseña) < 4:
        return "La contraseña no puede tener menos de 4 caracteres."
    return "La contraseña es válida."

# Solicitamos una contraseña al usuario
contraseña = input("Por favor, ingresa tu contraseña: ")

#como se puede poner como parametro que se necesite un numero?

#En este ejercicio tenes una variable de tipo list y una variable de tipo str. 
#Si corremos el código podemos probar que hay valores que serán modificados en el transcurso del código 
#y también habrá valores por referencia que no serán modificados.

#lista = ['a', 'b', 'c', 'd']
#texto = 'Hola'

#def multi(valor, referencia):
#    valor*=2
#    referencia*=2
#    print('durante el valor es', valor, ' y la referencia es ', referencia)


#print('Antes el valor era', texto, ' y la referencia era ', lista)
#multi(lista, texto)
#print('Despues el valor es', lista, ' y la referencia es ', texto)