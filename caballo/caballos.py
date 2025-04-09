# caballo/caballos.py
from database.db import guardar_caballo_result  # Nueva importación

class Caballo:
    def __init__(self, n):
        self.n = n
        self.tablero = [[-1 for _ in range(n)] for _ in range(n)]
        self.movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def es_seguro(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.tablero[x][y] == -1

    def resolver(self, x, y, movimiento):
        if movimiento == self.n * self.n:
            return True

        for i in range(8):
            nuevo_x = x + self.movimientos_x[i]
            nuevo_y = y + self.movimientos_y[i]
            if self.es_seguro(nuevo_x, nuevo_y):
                self.tablero[nuevo_x][nuevo_y] = movimiento
                if self.resolver(nuevo_x, nuevo_y, movimiento + 1):
                    return True
                self.tablero[nuevo_x][nuevo_y] = -1
        return False

    def mostrar_tablero(self):
        # Convertir el tablero a una cadena para mostrar
        output = "   "
        for col in range(self.n):
            output += f" {col:2} "
        output += "\n  +" + "----+" * self.n + "\n"

        for fila in range(self.n):
            output += f"{fila} |"
            for col in range(self.n):
                if self.tablero[fila][col] == -1:
                    output += "  . |"
                else:
                    output += f"{self.tablero[fila][col]:3} |"
            output += "\n  +" + "----+" * self.n + "\n"
        return output

def resolver_caballo(n=8, start_x=0, start_y=0):
    mensaje = f"Resolviendo el problema del recorrido del caballo (Knight's Tour) en un tablero {n}x{n}...\n"
    mensaje += f"Posición inicial del caballo: ({start_x}, {start_y})\n"
    
    if start_x < 0 or start_x >= n or start_y < 0 or start_y >= n:
        mensaje += f"Error: La posición inicial ({start_x}, {start_y}) está fuera del tablero {n}x{n}."
        return mensaje, None

    caballo = Caballo(n)
    caballo.tablero[start_x][start_y] = 0
    if caballo.resolver(start_x, start_y, 1):
        mensaje += "Solución encontrada:\n"
        mensaje += caballo.mostrar_tablero()
        
        # Guardar automáticamente el resultado en la base de datos
        guardar_caballo_result(tablero_size=n, start_x=start_x, start_y=start_y, recorrido=caballo.tablero)
        mensaje += "Resultado guardado automáticamente en la base de datos.\n"
        
        return mensaje, caballo.tablero
    else:
        mensaje += "No se encontró solución."
        return mensaje, None

if __name__ == "__main__":
    texto, _ = resolver_caballo(n=8, start_x=0, start_y=0)
    print(texto)