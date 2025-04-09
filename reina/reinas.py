# reina/reinas.py
from database.db import guardar_reinas_result  # Nueva importación

class Reinas:
    def __init__(self, n=8):
        self.n = n
        self.tablero = [-1] * n
        self.soluciones = []

    def es_seguro(self, fila, col):
        for prev_col in range(col):
            prev_fila = self.tablero[prev_col]
            if prev_fila == fila:
                return False
            if abs(prev_fila - fila) == abs(prev_col - col):
                return False
        return True

    def resolver(self, col=0):
        if col == self.n:
            self.soluciones.append(self.tablero[:])
            return

        for fila in range(self.n):
            if self.es_seguro(fila, col):
                self.tablero[col] = fila
                self.resolver(col + 1)
                self.tablero[col] = -1

    def obtener_soluciones(self):
        self.soluciones = []
        self.resolver()
        return self.soluciones

    def mostrar_tablero(self, solucion):
        # Convertir el tablero a una cadena para mostrar
        output = "   "
        for col in range(self.n):
            output += f" {col} "
        output += "\n  +" + "---+" * self.n + "\n"

        for fila in range(self.n):
            output += f"{fila} |"
            for col in range(self.n):
                if solucion[col] == fila:
                    output += " Q |"
                else:
                    output += " . |"
            output += "\n  +" + "---+" * self.n + "\n"
        return output

    def tablero_binario(self, solucion):
        # Convertir una solución a una matriz binaria para visualización
        tablero = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for col, fila in enumerate(solucion):
            tablero[fila][col] = 1
        return tablero

def resolver_reinas(n=8, max_soluciones_mostrar=3):
    mensaje = f"\n=== Iniciando el Problema de las {n} Reinas ===\n"
    try:
        mensaje += f"Resolviendo el problema de las {n} reinas...\n"
        
        reinas = Reinas(n)
        soluciones = reinas.obtener_soluciones()
        mensaje += f"Se encontraron {len(soluciones)} soluciones.\n"
        
        # Guardar automáticamente los resultados en la base de datos
        guardar_reinas_result(tablero_size=n, soluciones=soluciones)
        mensaje += "Resultados guardados automáticamente en la base de datos.\n"
        
        if not soluciones:
            mensaje += "No se encontraron soluciones.\n"
            mensaje += "=== Problema Finalizado ===\n"
            return mensaje, None

        # Mostrar hasta max_soluciones_mostrar soluciones
        for i, solucion in enumerate(soluciones[:max_soluciones_mostrar]):
            mensaje += f"\nSolución {i + 1}:\n"
            mensaje += reinas.mostrar_tablero(solucion)
        
        if len(soluciones) > max_soluciones_mostrar:
            mensaje += f"(Y {len(soluciones) - max_soluciones_mostrar} soluciones más...)\n"
        
        mensaje += "=== Problema Finalizado ===\n"
        
        # Devolver la primera solución como matriz binaria para visualización
        tablero = reinas.tablero_binario(soluciones[0])
        return mensaje, tablero
    
    except Exception as e:
        mensaje += f"Error al ejecutar el problema de las reinas: {e}\n"
        mensaje += "=== Problema Finalizado ===\n"
        return mensaje, None

if __name__ == "__main__":
    texto, _ = resolver_reinas(n=8, max_soluciones_mostrar=3)
    print(texto)