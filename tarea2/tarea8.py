llantas = int(input("Ingrese la cantidad de llantas que va a comprar: "))
if(llantas <=5):
    totala = llantas * 240000
    print("El valoe es de: ",totala)
elif (llantas >=6) and (llantas <=7):
    totalb = llantas * 221000
    print("El valoe es de: ",totalb)
elif (llantas >=8):
    totalc = llantas * 180000
    print("El valoe es de: ",totalc)