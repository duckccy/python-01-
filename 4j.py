# Solicitar el nombre del estudiante
nombre = input("Ingrese el nombre del estudiante: ")

# Solicitar las notas de las 3 evaluaciones
nota1 = float(input("Ingrese la nota de la evaluación 1 (1-20): "))
nota2 = float(input("Ingrese la nota de la evaluación 2 (1-20): "))
nota3 = float(input("Ingrese la nota de la evaluación 3 (1-20): "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar si aprobó o reprobó
if promedio > 12:
    estado = "Aprobó"
else:
    estado = "Reprobó"

# Imprimir el boletín del estudiante
print("\n--- Boletín del Estudiante ---")
print(f"Nombre: {nombre}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")
