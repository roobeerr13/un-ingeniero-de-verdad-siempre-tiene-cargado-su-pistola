# torre_de_hanoi/hanoi.py
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
        # Convertir el estado de las torres a una cadena
        output = "\nEstado actual de las torres:\n"
        max_altura = self.n
        for nivel in range(max_altura - 1, -1, -1):
            linea = ""
            for torre in ["A", "B", "C"]:
                if nivel < len(self.torres[torre]):
                    disco = self.torres[torre][nivel]
                    linea += " " * (self.n - disco) + "*" * (2 * disco - 1) + " " * (self.n - disco) + "  "
                else:
                    linea += " " * (self.n - 1) + "|" + " " * (self.n - 1) + "  "
            output += linea + "\n"
        output += "  Torre A     Torre B     Torre C  \n"
        return output

    def torre_de_hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            movimiento = f"Mover disco 1 de {origen} a {destino}"
            self.movimientos.append(movimiento)
            return movimiento
        movimiento1 = self.torre_de_hanoi(n - 1, origen, destino, auxiliar)
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        movimiento = f"Mover disco {n} de {origen} a {destino}"
        self.movimientos.append(movimiento)
        movimiento2 = self.torre_de_hanoi(n - 1, auxiliar, origen, destino)
        return f"{movimiento1}\n{movimiento}\n{movimiento2}" if movimiento1 and movimiento2 else movimiento

def resolver_torre_de_hanoi(n=3):
    mensaje = f"Resolviendo el problema de la Torre de Hanoi con {n} discos...\n"
    try:
        if n <= 0:
            mensaje += "Error: El número de discos debe ser positivo.\n"
            return mensaje

        juego = TorreDeHanoi(n)
        mensaje += "Estado inicial:\n"
        mensaje += juego.mostrar_torres()
        
        movimientos = juego.torre_de_hanoi(n, "A", "B", "C")
        for movimiento in juego.movimientos:
            mensaje += f"{movimiento}\n"
            mensaje += juego.mostrar_torres()
        
        # Guardar automáticamente los movimientos en la base de datos
        guardar_hanoi_result(num_discos=n, movimientos=juego.movimientos)
        mensaje += "Movimientos guardados automáticamente en la base de datos.\n"
        
        return mensaje
    
    except Exception as e:
        mensaje += f"Error al resolver el problema de la Torre de Hanoi: {e}\n"
        return mensaje

if __name__ == "__main__":
    texto = resolver_torre_de_hanoi(n=3)
    print(texto)