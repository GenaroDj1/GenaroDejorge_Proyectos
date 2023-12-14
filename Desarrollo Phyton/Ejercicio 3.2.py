# Si el precio es mayor a 100 pesos argentinos, entonces el descuento será del 20%, sino, el descuento será del 10%.
# (precio *= 0.8)
precio = float(input("Ingresa el precio del producto: "))

if(precio>100):
    print("descuento del 20%")
else:
    print("descuento del 10%")

