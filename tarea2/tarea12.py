print("Pulsaciones cada 10 seg")

edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero. F - M: ")

if genero == "F":
    pulsaciones = (220-edad)/10
    print("Sus pulsaciones es de: ", pulsaciones)
elif genero == "M":
    pulsaciones = (210-edad)/10
    print("Sus pulsaciones es de: ", pulsaciones)
else:
    print("Genero desconocido")