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
        print("   ", end="")
        for col in range(self.n):
            print(f" {col:2} ", end="")
        print("\n  +" + "----+" * self.n)

        for fila in range(self.n):
            print(f"{fila} |", end="")
            for col in range(self.n):
                if self.tablero[fila][col] == -1:
                    print("  . |", end="")
                else:
                    print(f"{self.tablero[fila][col]:3} |", end="")
            print("\n  +" + "----+" * self.n)
        print()

def resolver_caballo(n=8, start_x=0, start_y=0):
    print(f"Resolviendo el problema del recorrido del caballo (Knight's Tour) en un tablero {n}x{n}...")
    print(f"Posición inicial del caballo: ({start_x}, {start_y})")
    
    if start_x < 0 or start_x >= n or start_y < 0 or start_y >= n:
        print(f"Error: La posición inicial ({start_x}, {start_y}) está fuera del tablero {n}x{n}.")
        return

    caballo = Caballo(n)
    caballo.tablero[start_x][start_y] = 0
    if caballo.resolver(start_x, start_y, 1):
        print("Solución encontrada:")
        caballo.mostrar_tablero()
    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    resolver_caballo(n=8, start_x=0, start_y=0)