nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la primera nota: "))
nota3 = float(input("Ingrese la primera nota: "))
nota4 = float(input("Ingrese la primera nota: "))
nota5 = float(input("Ingrese la primera nota: "))
promedio = (nota1+nota2+nota3+nota4+nota5)/5
if (promedio>=3.0):
    print("El estudiante aprobo con: ", promedio)
else:
    print("El estudiante no aprobo con: ", promedio)