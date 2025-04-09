def agregar_al_archivo(alumno):
    with open("Registro_de_alumnos.txt","a") as Registro_de_alumnos:
        Registro_de_alumnos.write(alumno)
        Registro_de_alumnos.write("\n")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["NOMBRE"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["APELLIDO"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["DNI"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["FECHA DE NACIMIENTO"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["TUTOR"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["NOTAS"])
        Registro_de_alumnos.write(datos["alumnos"][alumno]["FALTAS"] + " - ")
        Registro_de_alumnos.write(datos["alumnos"][alumno]["AMONESTACIONES"])
        Registro_de_alumnos.write("\n")
def mostrar_operación(datos_a_mostrar):
    print("La operación se realizó correctamente.")
    print(datos_a_mostrar)

def ingresar_o_modificar_nombre(alumno):
    alumno["NOMBRE"] = "Nombre: " + input("Ingrese el nombre del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_apellido(alumno):
    alumno["APELLIDO"] = "Apellido: " + input("Ingrese el apellido del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_DNI(alumno):
    alumno["DNI"] = "DNI: " + input("Ingrese el DNI del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_fecha_de_nacimiento(alumno):
    alumno["FECHA DE NACIMIENTO"] = "Nacimiento: " + input("Ingrese la fecha de nacimiento del alumno(xx/xx/xxxx):")
    mostrar_operación(alumno)

def ingresar_o_modificar_tutor(alumno):
    alumno["TUTOR"] = "Tutor: " + input("Ingrese el nombre y apellido del tutor: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_notas(alumno):
    print("Ingrese todas las notas del alumno: ")
    alumno["NOTAS"] = "Notas: "
    while True:
        nota = input("Ingrese una nota (para dejar de ingresar, coloque 0): ")
        if nota == "0":
            break
        else:
            alumno["NOTAS"] = alumno["NOTAS"] + nota + " - "
    mostrar_operación(alumno)

def ingresar_o_modificar_faltas(alumno):
    alumno["FALTAS"] = "Faltas: " + input("Ingrese la cantidad total de faltas del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_amonestaciones(alumno):
    alumno["AMONESTACIONES"] = "Amonestaciones: " + input("Ingrese la cantidad total de amonestaciones del alumno:")
    mostrar_operación(alumno)

def modificar(lista):
    alumno_a_modificar = "alumno_" + input("Ingrese el número del alumno el cual desea modificar sus datos: ")
    dato_a_modificar = input("Ingrese el dato que desea modificar: ").upper()
    if dato_a_modificar == "NOMBRE":
        ingresar_o_modificar_nombre(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "APELLIDO":
        ingresar_o_modificar_apellido(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "DNI":
        ingresar_o_modificar_DNI(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "FECHA DE NACIMIENTO":
        ingresar_o_modificar_fecha_de_nacimiento(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "TUTOR":
        ingresar_o_modificar_tutor(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "NOTAS":
        ingresar_o_modificar_notas(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "FALTAS":
        ingresar_o_modificar_faltas(lista["alumnos"][alumno_a_modificar])
    elif dato_a_modificar == "AMONESTACIONES":
        ingresar_o_modificar_amonestaciones(lista["alumnos"][alumno_a_modificar])
    else:
        print("Error al ingresar el tipo de dato, ingrese nuevamente")
    

def ver(lista):
    ver_respuesta = input("Ingrese el número del alumno el cual desea ver sus datos: ")
    print(lista["alumnos"]["alumno_" + ver_respuesta])

def agregar(lista):
    alumno_a_agregar = "alumno_" + input("Ingrese el número del alumno el cual desea agregar: ")
    lista["alumnos"][alumno_a_agregar] = {}
    ingresar_o_modificar_nombre(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_apellido(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_DNI(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_fecha_de_nacimiento(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_tutor(lista["alumnos"][alumno_a_agregar]) 
    ingresar_o_modificar_notas(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_faltas(lista["alumnos"][alumno_a_agregar])
    ingresar_o_modificar_amonestaciones(lista["alumnos"][alumno_a_agregar])
    agregar_al_archivo(alumno_a_agregar)

    mostrar_operación(datos["alumnos"])

def eliminar(lista):
    alumno_a_eliminar = "alumno_" + input("Ingrese el número del alumno el cual desea eliminar: ")
    lista["alumnos"].pop(alumno_a_eliminar)
    mostrar_operación(datos["alumnos"])

with open("Registro_de_alumnos.txt","r+") as Registro_de_alumnos:
    datos = {"alumnos":{"alumno_1":{"NOMBRE":"Nombre: Danilo","APELLIDO":"Apellido: Mejia","DNI":"DNI: 46789584","FECHA DE NACIMIENTO":"Nacimiento: 19/04/2006","TUTOR":"Tutor: MARIANA BERRIOS", "NOTAS": "Notas: 4, 6, 5, 7, 2", "FALTAS": "Faltas: 11", "AMONESTACIONES": "Amonestaciones: 5"},"alumno_2":{"NOMBRE":"Nombre: Julian","APELLIDO":"Apellido: Sardinas","DNI":"DNI: 46791825","FECHA DE NACIMIENTO":"Nacimiento: 03/06/2006","TUTOR":"Tutor: SILVINA BELMONTE", "NOTAS": "Notas: 1, 2, 4, 5, 9", "FALTAS": "Faltas: 16", "AMONESTACIONES": "Amonestaciones: 2"}}}

    while True:
        x = Registro_de_alumnos.readlines()
        print(x)
        print()
        print("Bienvenido al registro de alumnos de la escuela")
        print("Que operación desea realizar con los datos de los alumnos: (modificar / ver / agregar / eliminar / ninguna)")
        respuesta = input().lower()

        if respuesta == "modificar":
            modificar(datos)
        
        elif respuesta == "ver":
            ver(datos)
        
        elif respuesta == "agregar":
            agregar(datos)
        
        elif respuesta == "eliminar":
            eliminar(datos)

        elif respuesta == "ninguna":
            break
        
        else:
            print("Error, ingrese nuvamente.")