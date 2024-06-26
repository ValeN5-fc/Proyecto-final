class Tarea:
    def __init__(self, descripcion):
        # Inicializamos la tarea con una descripcion y un estado incompleto
        self.descripcion = descripcion
        self.completada = False

def mostrar_menu():
    # Mostramos el menu principal y las opciones para el usuario
    print("\nMenú de tareas:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Mostrar tareas")
    print("5. Salir")
    return int(input("Seleccione una opción: "))

def agregar_tarea(tareas):
    # Agregamos una tarea a la lista
    descripcion = input("Ingrese la descripción de la tarea: ")
    tareas.append(Tarea(descripcion))
    print("¡Tarea agregada!")

def eliminar_tarea(tareas):
    # Eliminamos una tarea de la lista
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el índice de la tarea a eliminar: "))
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("¡Tarea eliminada!")
    else:
        print("¡Índice no válido!")

def marcar_tarea_completada(tareas):
    # Marcamos la tarea como completada
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
    if 0 <= indice < len(tareas):
        tareas[indice].completada = True
        print("¡Tarea marcada como completada!")
    else:
        print("¡Índice no válido!")

def mostrar_tareas(tareas):
    # Mostramos todas las tareas con su estado (completada o pendiente)
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea.completada else "Pendiente"
        print(f"{i}. {tarea.descripcion} [{estado}]")

def main():
    tareas = []
    while True:
        # Aqui muestra el menú y obtiene la opción seleccionada por el usuario
        opcion = mostrar_menu()
        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            eliminar_tarea(tareas)
        elif opcion == 3:
            marcar_tarea_completada(tareas)
        elif opcion == 4:
            mostrar_tareas(tareas)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("¡Opción no válida!")

if __name__ == "__main__":
    # Se veridica si se está ejecutando como el programa principal
    main()
