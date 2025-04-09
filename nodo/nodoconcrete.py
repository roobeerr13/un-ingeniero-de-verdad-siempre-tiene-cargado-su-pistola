from nodo import Nodo

class NodoConcreto(Nodo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.siguiente = None

    def movimientos_validos(self, n, visitados):
        posibles = [
            (self.x + 2, self.y + 1),
            (self.x + 2, self.y - 1),
            (self.x - 2, self.y + 1),
            (self.x - 2, self.y - 1),
            (self.x + 1, self.y + 2),
            (self.x + 1, self.y - 2),
            (self.x - 1, self.y + 2),
            (self.x - 1, self.y - 2),
        ]

        return [(nx, ny) for nx, ny in posibles if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visitados]