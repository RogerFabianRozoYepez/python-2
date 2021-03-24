precio = int(input("Ingrese el valor unitario del articulo: "))
articulo = int(input("Ingrese el numero de articulos: "))
total= precio*articulo
if articulo <5:
    print("Precio total a pagar es: ", total)
elif articulo >=5 and articulo<10:
    rest = (precio*5/(100))*(articulo)
    total1 = total-rest
    print("Precio total a pagar es: ", total1)
elif articulo>=10:
    rest = (precio*8/(100))*(articulo)
    total2 = total-rest
    print("Precio total a pagar es: ", total2)