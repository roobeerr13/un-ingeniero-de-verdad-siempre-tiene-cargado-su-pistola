class Lanzador:
    def __init__(self):
        self.movimientos = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],  # El 5 no tiene movimientos válidos
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

    def calcular_caminos(self, posicion, pasos_restantes):
        if pasos_restantes == 0:
            return 1  # Si no quedan pasos, este es un camino válido

        total_caminos = 0
        for siguiente_posicion in self.movimientos[posicion]:
            total_caminos += self.calcular_caminos(siguiente_posicion, pasos_restantes - 1)

        return total_caminos

    def calcular_todos_los_caminos(self, pasos):
        total_caminos = 0
        for posicion_inicial in self.movimientos.keys():
            total_caminos += self.calcular_caminos(posicion_inicial, pasos - 1)
        return total_caminos


if __name__ == "__main__":
    lanzador = Lanzador()
    pasos = int(input("Introduce el número de movimientos del caballo: "))
    total_caminos = lanzador.calcular_todos_los_caminos(pasos)
    print(f"El número total de caminos posibles con {pasos} movimientos es: {total_caminos}")