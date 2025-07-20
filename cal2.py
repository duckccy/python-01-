import os  # Para limpiar la consola

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola

    # Solicitar dos números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    while True:  # Bucle para realizar la operación
        # Preguntar por la operación que desea realizar
        print("Seleccione la operación que desea realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Regresar al inicio...")

        operacion = input("Ingrese el número de la operación (1/2/3/4/5): ")

        # Realizar la operación correspondiente
        if operacion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
            break  # Salir del bucle de operaciones

        elif operacion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
            break  # Salir del bucle de operaciones

        elif operacion == '3':
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
            break  # Salir del bucle de operaciones

        elif operacion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
                break  # Salir del bucle de operaciones
            else:
                print("Error: No se puede dividir entre cero.")
                break  # Salir del bucle de operaciones

        elif operacion == '5':
            print("Regresando al inicio...")
            break  # Salir del bucle de operaciones para reiniciar

        else:
            print("Seleccione una opcion correcta.")

    input("Presione Enter para continuar...")  # Espera a que el usuario presione Enter antes de repetir
