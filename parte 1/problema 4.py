# Crear el diccionario para almacenar los contactos
agenda = {}

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto", nombre, "agregado con exito.")

# Función para buscar un contacto
def buscar_contacto(nombre):
    if nombre in agenda:
        print(nombre + ":", agenda[nombre])
    else:
        print("El contacto", nombre, "no existe.")

# Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto", nombre, "eliminado con exito.")
    else:
        print("El contacto", nombre, "no existe.")

# Función para mostrar todos los contactos
def mostrar_contactos():
    if agenda:
        print("Agenda telefonica:")
        for nombre, telefono in agenda.items():
            print(nombre + ":", telefono)
    else:
        print("La agenda esta vacia.")

# Función principal para el menú de la agenda
def menu():
    while True:
        print("\nAgenda Telefonica")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el telefono del contacto: ")
            agregar_contacto(nombre, telefono)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == '4':
            mostrar_contactos()
        elif opcion == '5':
            print("Saliendo de la agenda telefonica.")
            break
        else:
            print("Opcion no valida, por favor seleccione una opcion del 1 al 5.")

# Ejecutar el menú
menu()
