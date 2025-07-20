import os

# Categorías y archivos asociados
scripts_por_categoria = {
    "Calculadoras": ["cal.py", "cal1.py", "cal2.py"],
    "Ejercicios": ["ej1.py", "ej2.py", "e2.py", "e3.py"],
    "Principal": ["main_extra.py"],  # Cambia esto si usas otro nombre
    "Otros": ["4j.py", "22.py"]
}

def mostrar_menu():
    print("""\n
 _   _      _ _         _
| | | | ___| | | ___   | |
| |_| |/ _ \ | |/ _ \  | |
|  _  |  __/ | | (_) | |_|
|_| |_|\___|_|_|\___/   _
                       |_|
                                                   
→ Seleccione una categoria:        
""")
    for i, categoria in enumerate(scripts_por_categoria.keys(), 1):
        print(f"{i}. {categoria}")
    print("0. Salir")

def mostrar_scripts(categoria):
    scripts = scripts_por_categoria[categoria]
    print(f"\n--- {categoria} ---")
    for i, script in enumerate(scripts, 1):
        print(f"{i}. {script}")
    print("0. Volver")

def ejecutar_script(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
    print(f"\n⏳ Ejecutando: {ruta}\n")
    os.system(f"python \"{ruta}\"")
    input("\n✅ Script finalizado. Presiona Enter para volver al menú principal...")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("¡Vamos elije! → "))
        except ValueError:
            print("❌ Opción inválida.\n")
            continue

        if opcion == 0:
            print("👋 Saliendo del menú...")
            break

        categorias = list(scripts_por_categoria.keys())
        if 1 <= opcion <= len(categorias):
            categoria = categorias[opcion - 1]
            mostrar_scripts(categoria)

            try:
                sub_opcion = int(input("Selecciona un script para ejecutar: "))
            except ValueError:
                print("❌ Opción inválida.\n")
                continue

            if sub_opcion == 0:
                continue

            scripts = scripts_por_categoria[categoria]
            if 1 <= sub_opcion <= len(scripts):
                ejecutar_script(scripts[sub_opcion - 1])
            else:
                print("❌ Número fuera de rango.\n")
        else:
            print("❌ Categoría no válida.\n")

if __name__ == "__main__":
    main()
