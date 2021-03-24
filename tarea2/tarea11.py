peso = float(input("Digite su peso: "))
talla = float(input("Digite su estatura en metros: "))
imc = peso/(talla**2)
if imc<20:
    print("Esta desnutrido")
if imc>=20 and imc<30:
    print("Esta normal")
if imc>=30 and imc<35:
    print("Esta en sobrepeso grado 1")
if imc>=35 and imc<40:
    print("Esta en sobrepeso grado 2")
if imc>=40:
    print("Esta en sobrepeso grado 3")