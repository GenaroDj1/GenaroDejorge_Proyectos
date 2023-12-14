#Sabemos que las mujeres se jubilan a los 60 años, y los hombres a los 65. ¿Qué datos deberíamos pedir para evaluarlos? Es importante que puedas dar un mensaje que muestre los resultados en cada caso.

genero= input("Ingrese su genero:")
edad= int(input("Ingrese su edad:"))


if (genero == "Hombre"):
    if(edad>=65):
        print("Cumplio sus años de asignación")
    else:
        print("Todavia es joven")
if (genero == "Mujer"):
    if (edad>=60):
        print("Cumplio sus años de asignación")
    else:
        print("Todavia es joven")