#Te damos un número : 150. Mediante el uso de código y todo lo que vimos, 
#te pedimos que muestres los 5 números anteriores y posteriores. 
#Siempre evaluando de no pasarnos con los números. 

for i in range(145, 151, 1):
            print ({i})
for x in range(151, 161, 1):
        print ({x})

x=145
i=160
while (x<=150 and i>=150):
    print({x}, {i})
    x+=1
    i-=1