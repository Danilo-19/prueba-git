def mostrar_operación(datos_a_mostrar):
    print("La operación se realizó correctamente.")
    print(datos_a_mostrar)

def ingresar_o_modificar_nombre(alumno):
    alumno["NOMBRE"] = input("Ingrese el nombre del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_apellido(alumno):
    alumno["APELLIDO"] = input("Ingrese el apellido del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_DNI(alumno):
    alumno["DNI"] = input("Ingrese el DNI del alumno: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_fecha_de_nacimiento(alumno):
    alumno["FECHA DE NACIMIENTO"] = input("Ingrese la fecha de nacimiento del alumno:")
    mostrar_operación(alumno)

def ingresar_o_modificar_tutor(alumno):
    alumno["TUTOR"] = input("Ingrese el nombre y apellido del tutor: ")
    mostrar_operación(alumno)

def ingresar_o_modificar_notas(alumno):
    alumno["NOTAS"] = []
    print("Ingrese todas las notas del alumno: ")
    while True:
        nota = int(input("Ingrese una nota (para dejar de ingresar, coloque 11): "))
        if nota == 11:
            break
        else:
            alumno["NOTAS"].append(nota)   
    mostrar_operación(alumno)

def ingresar_o_modificar_faltas(alumno):
    alumno["FALTAS"] = int(input("Ingrese la cantidad total de faltas del alumno: "))
    mostrar_operación(alumno)

def ingresar_o_modificar_amonestaciones(alumno):
    alumno["AMONESTACIONES"] = int(input("Ingrese la cantidad total de amonestaciones del alumno:"))
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
    mostrar_operación(datos["alumnos"])

def eliminar(lista):
    alumno_a_eliminar = "alumno_" + input("Ingrese el número del alumno el cual desea eliminar: ")
    lista["alumnos"].pop(alumno_a_eliminar)
    mostrar_operación(datos["alumnos"])




while True:

    datos = {"alumnos":{"alumno_1":{"NOMBRE":"Danilo","APELLIDO":"Mejia","DNI":"46789584","FECHA DE NACIMIENTO":"19/04/2006","TUTOR":"MARIANA BERRIOS","NOTAS":[4, 6, 5, 7, 2],"FALTAS":11,"AMONESTACIONES":5},"alumno_2":{"NOMBRE":"Julián","APELLIDO":"Sardinas","DNI":"46791925","FECHA DE NACIMIENTO":"03/06/2006","TUTOR":"Silvina Belmonte","NOTAS":[3, 4, 5, 1, 7],"FALTAS":15,"AMONESTACIONES":2}}}
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