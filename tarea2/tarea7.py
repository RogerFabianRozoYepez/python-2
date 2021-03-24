pago= int(float(input("Ingrese el valor de pago: ")))
if (pago<=149999):
    print("Su pago sera en efectivo", pago)
elif (pago>=150000)and(pago<=300000):
    print("Su pago sera pago con el celular", pago)
elif (pago>300000)and(pago<=600000):
    print("Su pago sera en tarjeta de debito", pago)
elif (pago>600000):
    print("Su pago sera en tarjeta de creddito", pago)