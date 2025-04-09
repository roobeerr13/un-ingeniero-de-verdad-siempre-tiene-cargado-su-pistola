from nodo.nodoconcrete import NodoConcreto

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, x, y):
        nuevo_nodo = NodoConcreto(x, y)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"({actual.x}, {actual.y})", end=" -> ")
            actual = actual.siguiente
        print("None")