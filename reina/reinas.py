class Reinas:
    def __init__(self, n=8):
        self.n = n  # Tamaño del tablero (8x8 por defecto)
        self.tablero = [-1] * n  # Representa las posiciones de las reinas: tablero[col] = fila
        self.soluciones = []  # Almacena todas las soluciones encontradas

    def es_seguro(self, fila, col):
        """
        Verifica si es seguro colocar una reina en la posición (fila, col).
        Revisa conflictos en filas, columnas y diagonales.
        """
        for prev_col in range(col):
            prev_fila = self.tablero[prev_col]
            if prev_fila == fila:
                return False
            if abs(prev_fila - fila) == abs(prev_col - col):
                return False
        return True

    def resolver(self, col=0):
        """
        Resuelve el problema de las N reinas usando backtracking.
        col: columna actual en la que estamos intentando colocar una reina.
        """
        if col == self.n:
            self.soluciones.append(self.tablero[:])
            return

        for fila in range(self.n):
            if self.es_seguro(fila, col):
                self.tablero[col] = fila
                self.resolver(col + 1)
                self.tablero[col] = -1

    def obtener_soluciones(self):
        """
        Devuelve todas las soluciones encontradas.
        """
        self.soluciones = []
        self.resolver()
        return self.soluciones

    def mostrar_tablero(self, solucion):
        """
        Muestra una solución en forma de tablero con bordes y etiquetas.
        """
        print("   ", end="")
        for col in range(self.n):
            print(f" {col} ", end="")
        print("\n  +" + "---+" * self.n)

        for fila in range(self.n):
            print(f"{fila} |", end="")
            for col in range(self.n):
                if solucion[col] == fila:
                    print(" Q |", end="")
                else:
                    print(" . |", end="")
            print("\n  +" + "---+" * self.n)
        print()

def resolver_reinas(n=8, max_soluciones_mostrar=3):
    """
    Resuelve el problema de las N reinas y muestra las soluciones.
    
    Args:
        n (int): Tamaño del tablero (por defecto 8 para 8 reinas).
        max_soluciones_mostrar (int): Número máximo de soluciones a mostrar.
    """
    print(f"\n=== Iniciando el Problema de las {n} Reinas ===")
    try:
        print(f"Resolviendo el problema de las {n} reinas...\n")
        
        reinas = Reinas(n)
        soluciones = reinas.obtener_soluciones()
        print(f"Se encontraron {len(soluciones)} soluciones.\n")
        
        for i, solucion in enumerate(soluciones[:max_soluciones_mostrar]):
            print(f"Solución {i + 1}:")
            reinas.mostrar_tablero(solucion)
        
        if len(soluciones) > max_soluciones_mostrar:
            print(f"(Y {len(soluciones) - max_soluciones_mostrar} soluciones más...)")
    
    except Exception as e:
        print(f"Error al ejecutar el problema de las reinas: {e}")
    
    print("=== Problema Finalizado ===\n")

if __name__ == "__main__":
    resolver_reinas(n=8, max_soluciones_mostrar=3)