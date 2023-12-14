#Descripción:
#Este proyecto consistirá en desarrollar una herramienta de gestión de tareas, 
#donde los usuarios puedan crear y editar tareas de una lista.
#Entregables:
#Tendrán que entregar el código de Python que implemente las funcionalidades de gestión de tareas: 
#crear, editar tareas de una lista. La función recibirá como parámetro una lista 
#y realizará las modificaciones correspondientes.

def crear_lista(lista_canciones):
    Lista = input("Ingresa la nueva lista de canciones separadas por coma, por favor: ")
    nueva_lista = Lista.split(',')
    lista_canciones.extend(nueva_lista)

def editar_lista(lista_canciones):
    if not lista_canciones:
        print("No hay lista para editar.")
        return

    print("Lista de canciones:")
    for i, lista in enumerate(lista_canciones):
        print(f"{i + 1}. {lista}")

    lista_a_editar = int(input("Ingrese el número de la lista que desee editar: ")) - 1

    if lista_a_editar < 0 or lista_a_editar >= len(lista_canciones):
        print("Número de lista no encontrado.")
        return

    nueva_lista = input("Ingresa la nueva lista de canciones que quiera agregar: ")
    lista_canciones[lista_a_editar] = nueva_lista

def eliminar_lista(lista_canciones):
    if not lista_canciones:
        print("No hay lista de canciones para eliminar.")
        return

    print("Lista de canciones:")
    for i, lista in enumerate(lista_canciones):
        print(f"{i + 1}. {lista}")

    lista_a_eliminar = int(input("Ingrese el número de la lista que desee eliminar: ")) - 1

    if lista_a_eliminar < 0 or lista_a_eliminar >= len(lista_canciones):
        print("Número de lista no válido.")
        return

    lista_eliminada = lista_canciones.pop(lista_a_eliminar)
    print(f"Su lista fue eliminada: {lista_eliminada}")


listas = []  

while True:
    print("\n1. Crear lista de canciones")
    print("2. Editar lista")
    print("3. Eliminar lista")
    print("4. Salir del programa")
    
    opcion = input("Elija una opción: ")
    
    if opcion == '1':
        crear_lista(listas)
    elif opcion == '2':
        editar_lista(listas)
    elif opcion == '3':
        eliminar_lista(listas)
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

print("Lista de canciones final:", listas)
