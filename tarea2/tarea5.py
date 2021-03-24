from math import pi

print("(1) Calcular triangulo")
print("(2) Calcular circulo")
print("(3) Calcular cuadrado")
print("(4) Calcular trapecio")
print("(5) Calcular rectangulo")
print("(6) Calcular elipse")

consulta = int(input("Ingrese el valor: "))

if consulta == 1:
    print("Calcular el area del triangulo")
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = (base*altura)/2
    print ("El area del cuadrado es: ", area)

if consulta == 2:
    print("Calcular el area del circulo")
    r = float(input("Ingrese el valor del radio: "))
    area = pi * r ** 2
    print ("El area del circulo es: ", area)   

if consulta == 3:
    print("Calcular el area del cuadrado")
    lado = float(input("Ingrese el valor de un lado: "))
    area = lado*lado
    print ("El area del cuadrado es: ", area)

if consulta == 4:
    print("Calcular el area del trapecio")
    base1 = float(input("Ingrese el valor de una base: "))
    base2 = float(input("Ingrese el valor de una base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = (altura*(base1+base2))/2
    print ("El area del trapecio es: ", area)

if consulta == 5:
    print("Calcular el area del rectangulo")
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = base*altura
    print ("El area del rectangulo es: ", area)

if consulta == 6:
    print("Calcular el area del elipse")
    r1 = float(input("Ingrese el valor del radio 1: "))
    r2 = float(input("Ingrese el valor del radio 2: "))
    area = r1 * r2 * pi
    print ("El area de la elipse es: ", area)                