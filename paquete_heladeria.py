import paquete_restaurante

class Heladeria(paquete_restaurante.Restaurante):
    def __init__(self, nombre, comida, sabores):
        super().__init__(nombre, comida)
        self.lista_sabores = sabores

    def mostrar_saborares(self):
        print()
        print(f"Los sabores que tenemos son: ")
        print()
        for i in range(len(self.lista_sabores)):
            print(self.lista_sabores[i])