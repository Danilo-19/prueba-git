class Restaurante():
    
    def __init__(self, nombre, comida):
        self.restaurante_nombre = nombre
        self.tipo_comida = comida
        

    def describir_restaurante(self):
        print(f"Nuestro restaurante se llama {self.restaurante_nombre}")
        print(f"¡Vendemos {self.tipo_comida}!")
        

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} está abierto")