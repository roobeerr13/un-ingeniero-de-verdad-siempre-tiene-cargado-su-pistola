from database.db import guardar_hanoi_result  # Nueva importación

class TorreDeHanoi:
    def __init__(self, n):
        self.n = n
        self.torres = {
            "A": list(range(n, 0, -1)),
            "B": [],
            "C": []
        }
        self.movimientos = []  # Lista para almacenar los movimientos

    def mostrar_torres(self):
        print("\nEstado actual de las torres:")
        max_altura = self.n
        for nivel in range(max_altura - 1, -1, -1):
            linea = ""
            for torre in ["A", "B", "C"]:
                if nivel < len(self.torres[torre]):
                    disco = self.torres[torre][nivel]
                    linea += " " * (self.n - disco) + "*" * (2 * disco - 1) + " " * (self.n - disco) + "  "
                else:
                    linea += " " * (self.n - 1) + "|" + " " * (self.n - 1) + "  "
            print(linea)
        print("  Torre A     Torre B     Torre C  \n")

    def torre_de_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            movimiento = f"Mover disco 1 de {origen} a {destino}"
            self.movimientos.append(movimiento)
            print(movimiento)
            self.mostrar_torres()
            return
        self.torre_de_hanoi(n - 1, origen, destino, auxiliar)
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        movimiento = f"Mover disco {n} de {origen} a {destino}"
        self.movimientos.append(movimiento)
        print(movimiento)
        self.mostrar_torres()
        self.torre_de_hanoi(n - 1, auxiliar, origen, destino)

def resolver_torre_de_hanoi(n=3):
    print(f"Resolviendo el problema de la Torre de Hanoi con {n} discos...")
    juego = TorreDeHanoi(n)
    print("Estado inicial:")
    juego.mostrar_torres()
    juego.torre_de_hanoi(n, "A", "B", "C")
    
    # Guardar automáticamente los movimientos en la base de datos
    guardar_hanoi_result(num_discos=n, movimientos=juego.movimientos)
    print("Movimientos guardados automáticamente en la base de datos.\n")

if __name__ == "__main__":
    resolver_torre_de_hanoi(n=3)