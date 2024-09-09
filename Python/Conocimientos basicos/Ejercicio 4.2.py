# Calculadora de área de un rectangulo
print("Rectangulo")
base = float(input("ingrese el valor de la base: "))
altura = float(input("ingrese el valor de la altura: "))

ARectangulo = base*altura
print("El área del Rectangulo es:", ARectangulo)

print("Cuadrado")
Lado = float(input("ingrese el valor de la base: "))
Lado = float(input("ingrese el valor de la altura: "))

ACuadrado = Lado*Lado
print("El área del Cuadrado es:", ACuadrado)

print("Triangulo")
Base = float(input("ingrese el valor de la base: "))
Altura = float(input("ingrese el valor de la altura: "))

ATriangulo = (Base*Altura)/2
print("El área del Cuadrado es:", ATriangulo)

print("Trapecio")
Base1 = float(input("ingrese el valor de la base: "))
Base2 = float(input("ingrese el valor de la base: "))
ALtura = float(input("ingrese el valor de la altura: "))

ATrapecio = ((Base1+Base2)/2)*ALtura
print("El área del Cuadrado es:", ATrapecio)

print("Rombo")
distancia= float(input("ingrese el valor de la base: "))
Distancia = float(input("ingrese el valor de la altura: "))

ARombo = (distancia*Distancia)/2
print("El área del Cuadrado es:", ARombo)



