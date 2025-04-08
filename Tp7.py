# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

"""
class Rectangulo():
    def __init__(self, base_elegida, altura_elegida):
        self.base = base_elegida
        self.altura = altura_elegida
    
    def area(self):
        area = self.base * self.altura
        print(f"El área de tu rectángulo es: {area}")

b = int(input("Ingrese la base del rectángulo: "))
h = int(input("Ingrese la altura del rectángulo: "))

figura1 = Rectangulo(b,h)

figura1.area()
"""

# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
# La clase debe contener como miembros:
# - Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# - Un atributo para el estado (lleno o vacío).
# - Un atributo n, que indica la cantidad máxima de cebadas.
# - Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# - Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# - Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

"""
class Mate():
    def __init__(self, n):
        self.cantidad_cebadas_restantes = n
        self.cebado = False
        self.cantidad_max_cebadas = n
    def cebar(self):
        if self.cebado:
            print("¡Cuidado, te quemaste!")
        else:
            self.cebado = True
    def beber(self):
        if self.cebado:
            if self.cantidad_cebadas_restantes == 0:
                print("Advertencia: el mate está lavado.")
            else:
                self.cantidad_cebadas_restantes = self.cantidad_cebadas_restantes - 1
            self.cebado = False   
        else:
            print("¡El mate está vacío! *ruido de mate* ")

print("Usted va a tomar mate.")
print()
cantidad_maxima_cebadas = int(input("Ingrese cuantas veces se necesita cebar para que su mate esté lavado: "))
mate1 = Mate(cantidad_maxima_cebadas)

mate1.cebar()
mate1.beber()
mate1.beber()
mate1.beber()
mate1.cebar()
mate1.cebar()
mate1.beber()
mate1.cebar()
mate1.beber()
"""

# 3) Botella y Sacacorchos
# - Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# - Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
# destapada.
# - Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
# - Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
# un corcho.

"""
class Corcho():
    def __init__(self, nombre):
            self.nombre_de_la_bodega = nombre
            print(f"El corcho que tiene es de la bodega: {self.nombre_de_la_bodega}")
class Botella():
    def __init__(self, tapa):
        self.corcho = tapa
        if self.corcho:
            print(f"Tiene puesto el corcho")
        else:
            print(f"Está destapada")
class SacaCorchos():
    def __init__(self, botella, coso):
        self.botella = botella
        self.coso = coso

    def destapar(self,botella):
        if self.coso:
            print("El sacacorcho contiene un corcho")
        if self.botella.corcho:
            self.botella.corcho = False
            print("Acabas de sacar el corcho")
            self.coso = True
        else:
            print("La botella ya está destapada")

    def limpiar(self):
        if self.coso:
            self.coso = False
            print("Acabas de limpiar el sacacorcho")
        else:
            print("El sacacorchos no contiene ningún sacacorcho")


corcho1 = Corcho("El Porvenir")
botella1 = Botella(True)
sacacorchos = SacaCorchos(botella1, False)
 
sacacorchos.destapar(botella1)
sacacorchos.limpiar()
sacacorchos.destapar(botella1)
"""

# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método.

"""
class Restaurante():
    def __init__(self, nombre, comida):
        self.restaurante_nombre = nombre
        self.tipo_comida = comida
        

    def describir_restaurante(self):
        print(f"Nuestro restaurante se llama {self.restaurante_nombre}")
        print(f"¡Vendemos {self.tipo_comida}!")
        

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} está abierto")
        

class Heladeria(Restaurante):
    def __init__(self, nombre, comida, sabores):
        super().__init__(nombre, comida)
        self.lista_sabores = sabores

    def mostrar_saborares(self):
        print()
        print(f"Los sabores que tenemos son: ")
        print()
        for i in range(len(self.lista_sabores)):
            print(self.lista_sabores[i])

rosmari = Heladeria("Rosmari","Helado", ["Chocolate", "Vainilla", "Dulce de Leche", "Crema del Cielo","Frutilla"])

rosmari.describir_restaurante()
rosmari.abrir_restaurante()
rosmari.mostrar_saborares()
"""

# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
# - Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.
# - Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada

"""
import random
class Personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad
    
    def recibir_ataque(self, ataque):
        self.vida = self.vida - ataque
        if self.vida <= 0:
            print("MORISTE")
        else:
            print(f"Le dieron! ahora el soldado tiene {self.vida} de vida")
    
    def mover(self, direccion):
        if direccion == "adelante":
            self.posicion[0] = self.posicion[0] + self.velocidad
        elif direccion == "atras":
            self.posicion[0] = self.posicion[0] - self.velocidad
        elif direccion == "derecha":
            self.posicion[1] = self.posicion[1] + self.velocidad
        elif direccion == "izquierda":
            self.posicion[1] = self.posicion[1] - self.velocidad
        elif direccion == "arriba":
            self.posicion[2] = self.posicion[2] + self.velocidad
        elif direccion == "abajo":
            self.posicion[2] = self.posicion[2] - self.velocidad
    
class Soldado(Personaje):

    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque
    
    def atacar(self, victima):
        victima.recibir_ataque(self.ataque)
        print("Ha sufrido un ataque!")
    
class Campesino(Personaje):

    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha
    
    def cosechar(self):
        cantidad_a_cosechar = random.randint(1,9)
        if self.cosecha - cantidad_a_cosechar  >= 1:
            self.cosecha = self.cosecha - cantidad_a_cosechar
            return f"El campesino cosechó {cantidad_a_cosechar} puerros"
        else:
            return "Ya no hay más para cosechar"

soldado_aleman = Soldado(100, [0, 3, 4], 4, 11)
soldado_frances = Soldado(100, [5, 1, -2], 7, 13)
campesino_hungaro = Campesino(100, [0, 0, 0], 10, 50)

soldado_aleman.atacar(soldado_frances)
soldado_frances.mover("arriba")
cosechas = campesino_hungaro.cosechar()
print(cosechas)
"""

# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

"""
class Usuario():

    def __init__(self, nombre, apellido, mail, contraseña, usuario, telefono):
        self.nombres = nombre
        self.apellidos = apellido
        self.mail = mail
        self.cantraseña = contraseña
        self.usuario = usuario
        self.telefono = telefono

    def describir_usuario(self):
        print(f"Usuario: {self.usuario}")
        print(f"Nombre: {self.nombres}")
        print(f"Apellido: {self.apellidos}")

    def saludar_usuario(self):
        print(f"Que onda {self.usuario}. Ingresaste al server más argentino que verás en toda tu vida boeee, bienvenido pa.")

n = int(input("Ingrese la canitdad de usuarios totales que desea ingresar: "))
lista = []
for i in range(n):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    mail = input("Ingrese su mail: ")
    contraseña = input("Ingrese su contraseña (shh): ")
    usuario = input("Ingrese su nombre de usuario (nick name): ")
    telefono = input("Ingrese su número de teléfono: ")
    usuario = Usuario(nombre, apellido, mail, contraseña, usuario, telefono)
    lista.append(usuario)

for i in range(len(lista)):
    lista[i].describir_usuario()
    lista[i].saludar_usuario()
"""

# 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

"""
class Administrador(Usuario):

    privilegios = ["Puede postear en el foro", "puede borrar un post", "puede banear usuario"]
    
    def __inti__(self, nombre, apellido, mail, contraseña, usuario, telefono):
        super().__init__(nombre, apellido, mail, contraseña, usuario, telefono)
        
    
    def mostrar_privilegios(self, usuario):
        print(f"Felicidades {usuario} eres admin, estos son tus privilegios: ")
        print(self.privilegios)

print("Ingrese los datos del admin.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
mail = input("Ingrese su mail: ")
contraseña = input("Ingrese su contraseña (shh): ")
usuario = input("Ingrese su nombre de usuario (nick name)")
telefono = input("Ingrese su número de teléfono: ")
admin1 = Administrador(nombre, apellido, mail, contraseña, usuario, telefono)
admin1.mostrar_privilegios(usuario)
"""


# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios.

"""
class Privilegios():

    privilegios = ["puede postear en el foro", "puede borrar un post", "puede banear usuario", "tiene posteos ilimitados", "puede borrar posteos"]

    def mostrar_privilegios(self):
        print(f"Felicidades eres admin, estos son tus privilegios: ")
        print(self.privilegios)

class Administrador(Usuario):

    privilegios = Privilegios()
    def __inti__(self, nombre, apellido, mail, contraseña, usuario, telefono):
        super().__init__(nombre, apellido, mail, contraseña, usuario, telefono)
    
    def mostrar(self):
        self.privilegios.mostrar_privilegios()
    
    


print("Ingrese los datos del admin.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
mail = input("Ingrese su mail: ")
contraseña = input("Ingrese su contraseña (shh): ")
usuario = input("Ingrese su nombre de usuario (nick name)")
telefono = input("Ingrese su número de teléfono: ")
admin1 = Administrador(nombre, apellido, mail, contraseña, usuario, telefono)
admin1.mostrar()
"""

# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4,  e impórtela al módulo actual. 
# Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación funcionó.

"""
import paquete_restaurante
mamma_mia = paquete_restaurante.Restaurante("Mamma Mia", "Pastas")
mamma_mia.describir_restaurante()
"""

# 10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. 
# ¿Qué se necesita para que funcione la importación?

"""
import paquete_heladeria
freddo = paquete_heladeria.Heladeria("Freddo","Helado",["furtilla","limon","durazno","naranja"])
freddo.describir_restaurante()
freddo.mostrar_saborares()
"""



