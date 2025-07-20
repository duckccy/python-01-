# Solicitar al usuario que ingrese dos números
numero = float(input("Ingrese el numero: "))
calculo=0.0

if numero>= 0:
    calculo=numero
    
else: calculo=numero*-1

print(f"El valor absoluto de la variable: {numero} es {calculo}")