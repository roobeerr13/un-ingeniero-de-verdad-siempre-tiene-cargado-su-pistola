from database.db import guardar_vector, mostrar_vectores

def guardar_vector_manual():
    """
    Permite al usuario ingresar un vector y guardarlo en la base de datos.
    """
    print("\n=== Guardar un Vector ===")
    try:
        nombre = input("Ingresa el nombre del vector: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        print("Ingresa los elementos del vector (números separados por espacios):")
        elementos_input = input().strip()
        if not elementos_input:
            print("Debes ingresar al menos un número.")
            return

        try:
            elementos = [float(x) for x in elementos_input.split()]
        except ValueError:
            print("Error: Ingresa solo números válidos separados por espacios.")
            return

        if guardar_vector(nombre, elementos):
            print(f"Vector '{nombre}' guardado exitosamente con datos: {elementos}")

    except Exception as e:
        print(f"Error al guardar el vector: {e}")

def manejar_vectores():
    """
    Menú para manejar operaciones con vectores.
    """
    while True:
        print("\n+" + "-" * 30 + "+")
        print("|        Menú de Vectores      |")
        print("+" + "-" * 30 + "+")
        print("| 1. Guardar un vector         |")
        print("| 2. Mostrar todos los vectores|")
        print("| 3. Volver al menú principal  |")
        print("+" + "-" * 30 + "+")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            guardar_vector_manual()
        elif opcion == "2":
            mostrar_vectores()
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    manejar_vectores()