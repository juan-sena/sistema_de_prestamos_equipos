equipos = {
    "Laptop": {"disponible": True, "prestamo": []},
    "Tablet samsung": {"disponible": True, "prestamo": []},
    "Tablet apple": {"disponible": True, "prestamo": []},
    "Proyector": {"disponible": True, "prestamo": []},
}


def mostrar_equipos():
    print("==== Equipos del sistema ====")
    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print("Nombre:", nombre,)
        print("Estado:", estado)
        


def registrar_prestamo():
    mostrar_equipos()

    print("==== Registrar Prestamo ====")
    nombre = input("Ingrese el nombre del equipo:\n")
    if nombre not in equipos:
        print("El equipo no existe")
        return
    if equipos[nombre]["disponible"] == False:
        print("El equipo no esta disponible")
        return

    usuario = input("Ingrese su nombre:\n")
    fecha = input("Ingrese la fecha:\n")

    prestamo = (usuario, fecha)
    equipos[nombre]["prestamo"].append(prestamo)
    equipos[nombre]["disponible"] = False
    print("Prestamo registrado con exito")


def devolver_equipo():
    print("=== Devolver equipo ===")
    nombre = input("Ingrese el nombre del equipo:\n")
    if nombre not in equipos:
        print("El equipo no existe")
        return
    if equipos[nombre]["disponible"]:
        print("El equipo no esta prestado")
        return
    equipos[nombre]["disponible"] = True
    print("Equipo devuelto con exito")


def ver_historial():
    print("=== Historial de prestamos ===")
    tiene_prestamos = False
    for equipo, datos in equipos.items():
        if datos["prestamo"]:
            tiene_prestamos = True
            print("Equipo:", equipo)
            for prestamo in datos["prestamo"]:
                print("Usuario:", prestamo[0], "Fecha:", prestamo[1])
    if not tiene_prestamos:
        print("sin prestamos registrados")


def agregar_equipo():
    print("=== Agregar equipo ===")
    nombre = input("Ingrese el nombre del equipo:\n")
    if nombre in equipos:
        print("El equipo ya existe")
        return
    equipos[nombre] = {"disponible": True, "prestamo": []}
    print("Equipo agregado con exito")


def menu():
    while True:
        print("=== Sistema de prestamos de equipos ===")
        print("1. Ver equipos disponibles")
        print("2. Registrar prestamo")
        print("3. Devolver equipo")
        print("4. Ver historial de prestamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir del programa")
        opcion = input("Ingrese una opcion:")

        match opcion:
            case "1":
                mostrar_equipos()
            case "2":
                registrar_prestamo()
            case "3":
                devolver_equipo()
            case "4":
                ver_historial()
            case "5":
                agregar_equipo()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, intente nuevamente")


menu()