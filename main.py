from reina.reinas import resolver_reinas
from caballo.caballos import resolver_caballo
from torre_de_hanoi.hanoi import resolver_torre_de_hanoi
from vectores.vectores import manejar_vectores
from database.db import mostrar_reinas_results, mostrar_caballo_results, mostrar_hanoi_results  # Nuevas importaciones

def mostrar_menu():
    print("\n+" + "-" * 40 + "+")
    print("|           Menú de Juegos y Datos        |")
    print("+" + "-" * 40 + "+")
    print("| 1. Problema de las 8 Reinas            |")
    print("| 2. Recorrido del Caballo               |")
    print("| 3. Torre de Hanoi                      |")
    print("| 4. Manejar Vectores                    |")
    print("| 5. Mostrar Resultados de Reinas        |")
    print("| 6. Mostrar Resultados del Caballo      |")
    print("| 7. Mostrar Resultados de Hanoi         |")
    print("| 8. Salir                               |")
    print("+" + "-" * 40 + "+")

def obtener_entero(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"El valor debe ser al menos {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            print("\n--- Configuración del Problema de las Reinas ---")
            n = obtener_entero("Ingresa el tamaño del tablero (n): ", minimo=4)
            max_soluciones = obtener_entero("Ingresa el número máximo de soluciones a mostrar: ")
            resolver_reinas(n=n, max_soluciones_mostrar=max_soluciones)

        elif opcion == "2":
            print("\n--- Configuración del Recorrido del Caballo ---")
            n = obtener_entero("Ingresa el tamaño del tablero (n): ", minimo=5)
            start_x = obtener_entero(f"Ingresa la coordenada X inicial del caballo (0 a {n-1}): ", minimo=0)
            start_y = obtener_entero(f"Ingresa la coordenada Y inicial del caballo (0 a {n-1}): ", minimo=0)
            print("\n=== Iniciando el Juego ===")
            try:
                resolver_caballo(n=n, start_x=start_x, start_y=start_y)
            except Exception as e:
                print(f"Error al ejecutar el problema del caballo: {e}")
            print("=== Juego Finalizado ===\n")

        elif opcion == "3":
            print("\n--- Configuración de la Torre de Hanoi ---")
            n = obtener_entero("Ingresa el número de discos: ", minimo=1)
            print("\n=== Iniciando el Juego ===")
            try:
                resolver_torre_de_hanoi(n=n)
            except Exception as e:
                print(f"Error al ejecutar el problema de la Torre de Hanoi: {e}")
            print("=== Juego Finalizado ===\n")

        elif opcion == "4":
            print("\n=== Iniciando Manejo de Vectores ===")
            try:
                manejar_vectores()
            except Exception as e:
                print(f"Error al manejar vectores: {e}")
            print("=== Finalizado Manejo de Vectores ===\n")

        elif opcion == "5":
            print("\n=== Mostrando Resultados de Reinas ===")
            mostrar_reinas_results()
            print("=== Fin de Resultados ===\n")

        elif opcion == "6":
            print("\n=== Mostrando Resultados del Caballo ===")
            mostrar_caballo_results()
            print("=== Fin de Resultados ===\n")

        elif opcion == "7":
            print("\n=== Mostrando Resultados de Hanoi ===")
            mostrar_hanoi_results()
            print("=== Fin de Resultados ===\n")

        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()