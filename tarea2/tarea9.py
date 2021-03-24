print("Tamaño y precios: 1-15000 2-24000 3-36000")
pizza = int(input("Ibgresar el tamaño de la pizza: "))
ingredientes = int(input("Ingresar el numero de ingredientes extras: "))
total = ingredientes * 4000
if pizza == 1:
    print("Precio de la pizza a $15.000")
    total1= total + 15000
    print("El precio es: ", total1)
if pizza == 2:
    print("Precio de la pizza a $24.000")
    total2= total + 24000
    print("El precio es: ", total2)
if pizza == 3:
    print("Precio de la pizza a $36.000")
    total3= total + 36000
    print("El precio es: ", total3)
else:
    print("Opcion desconocida")