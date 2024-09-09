#Pedile a chetGPT que te genere una lista con 50 mensajes al azar de bienvenida... 
#Podríamos plantearnos las siguientes preguntas antes de preguntarle a chatGPT
#¿Cuál sería la mejor estructura para un mensaje de bienvenida?
#¿Puedo pedirle que siempre el mensaje comience con la palabra bienvenida?
#Lo correcto sería asignarle un número máximo de caracteres por mensaje. 
#¿Cuál crees que sería el mejor número para un mensaje de bienvenida?

import openai

# Configura tu clave de API de OpenAI
openai.api_key = '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'  

def generar_mensajes_bienvenida():
    prompt = "Bienvenida"
    temperatura = 0.7  # Ajusta la temperatura según tus preferencias (valores más bajos hacen que las respuestas sean más determinísticas)

    # Realiza la llamada a la API para generar mensajes de bienvenida
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes ajustar el motor según tus necesidades
        prompt=prompt,
        max_tokens=30,
        n=50,  # Generar 50 mensajes
        temperature=temperatura,
    )

    # Recopila y devuelve los mensajes generados
    mensajes_generados = [choice['text'].strip() for choice in response['choices']]
    return mensajes_generados

# Ejemplo de uso
mensajes_bienvenida = generar_mensajes_bienvenida()
for i, mensaje in enumerate(mensajes_bienvenida, start=1):
    print(f"{i}. {mensaje}")



#Ejercicio Opcional!

#Pedile a chatGPT que te genere una lista de python que te sirva para copiar y pegar en tu código, 
#con números 50 números al azar y sin repetir entre 0 y 200. Generá la función que te permita corroborar eso

#no permite generar numeros con la libreria open ai

import random

def generar_lista_numeros():
    # Generar una lista de 50 números al azar sin repetición en el rango de 0 a 20
    lista_numeros = random.sample(range(21), 50)
    return lista_numeros

def verificar_sin_repeticion(lista):
    # Verificar si no hay números repetidos en la lista
    return len(lista) == len(set(lista))

# Ejemplo de uso
lista_numeros_azar = generar_lista_numeros()
print("Lista de números al azar:", lista_numeros_azar)

# Verificar si no hay números repetidos
if verificar_sin_repeticion(lista_numeros_azar):
    print("La lista no tiene números repetidos.")
else:
    print("La lista tiene números repetidos.")
