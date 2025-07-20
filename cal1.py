while True:
    # Solicitar dos números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

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

    elif operacion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")

    elif operacion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif operacion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    
    elif operacion == '5':
        print("Regresando al inicio...")
        continue  # Repite el bucle para permitir nueva operación

    else:
        print("Operación no válida. Por favor, intente nuevamente.")
