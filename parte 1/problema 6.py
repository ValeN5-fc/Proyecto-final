# Definición de la clase Persona
class Persona:
    # Método especial __init__ para inicializar objetos de la clase con atributos nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asignación del nombre pasado como parámetro al atributo nombre del objeto
        self.edad = edad  # Asignación de la edad pasada como parámetro al atributo edad del objeto
    
    # Método para mostrar los datos de la persona
    def mostrar_datos(self):
        print("Nombre:", self.nombre, "Edad:", self.edad)

# Función para crear una instancia de Persona con datos ingresados por el usuario
def crear_persona():
    nombre = input("Ingrese el nombre de la persona: ")  # Solicitar al usuario que ingrese el nombre
    edad = int(input("Ingrese la edad de la persona: "))  # Solicitar al usuario que ingrese la edad
    return Persona(nombre, edad)  # Devolver una nueva instancia de Persona con los datos ingresados

# Ejemplo de uso:
print("Crear una persona:")
persona1 = crear_persona()  # Llamar a la función crear_persona para crear una nueva instancia de Persona
persona1.mostrar_datos()  # Llamar al método mostrar_datos para mostrar los datos de la persona creada
