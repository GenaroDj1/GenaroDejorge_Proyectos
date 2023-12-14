#Crea una función que te de un mensaje de error si la contraseña que ingresamos 
#por un input tiene estos problemas:

#Tiene una letra ñ.
#Tiene espacios, ya sea delante, en el medio o atras.
#Si tiene mas de 8 caracteres.
#Si tiene menos de 4 caracteres

def ContraseñaSegura (contrasenia):
     if 'ñ' in contrasenia:
        return "La contraseña no puede contener la letra 'ñ'."
     else:
        if ' ' in contrasenia:
            return "La contraseña no puede contener espacios."
        if len(contrasenia) > 8:
             return "La contraseña no puede tener más de 8 caracteres."
        if len(contrasenia) < 4:
            return "La contraseña no puede tener menos de 4 caracteres."
        return "La contraseña es válida."
contrasenia= input("Por favor, escriba su contraseña: ")
resultado = ContraseñaSegura(contrasenia)
print(resultado)

#Crea una función que te indique si el valor ingresado no cumple con estos requisitos:
#El numero ingresado tiene que ser mayor a 20000000
#Tiene que tener hasta nueve dígitos.

def Valoringresado (Valor):
    if (Valor <20000000):
        return "El valor debe ser mayor a 20000000"
    if len(Valor)<9:
        return("El numero ingresado debe ser mayor a 9 digitos")
    return ("Numero Valido")
Valor= int(input("Ingrese un valor numerico por favor: "))
ValorIngresado= Valoringresado(Valor)
print(ValorIngresado)



