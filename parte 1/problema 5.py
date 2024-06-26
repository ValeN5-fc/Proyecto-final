# Definición de la función para escribir en un archivo
def Escribir_archivo():
    # Solicitar al usuario que ingrese el nombre del archivo a escribir
    nombre_archivo = input("Ingrese el nombre del archivo a escribir: ")
    nombre_archivo = nombre_archivo + ".txt"  # Agregar extensión .txt al nombre del archivo
    
    # Abrir el archivo en modo escritura ('w') usando 'with' para garantizar el cierre automático del archivo
    with open(nombre_archivo, 'w') as archivo:
        # Solicitar al usuario que ingrese el texto a escribir en el archivo
        texto = input("Digite un texto para escribir en el archivo: ")
        # Escribir el texto en el archivo, agregando un salto de línea al final
        archivo.write(texto + "\n")
    
    # Imprimir un mensaje para confirmar que el texto se ha escrito correctamente en el archivo
    print("Texto escrito en el archivo correctamente")

# Definición de la función para leer un archivo
def Leer_archivo():
    # Solicitar al usuario que ingrese el nombre del archivo a leer
    nombre_archivo = input("Digite el nombre del archivo a leer: ")
    nombre_archivo += ".txt"  # Agregar extensión .txt al nombre del archivo
    
    try:
        # Intentar abrir el archivo en modo lectura ('r') usando 'with' para garantizar el cierre automático del archivo
        with open(nombre_archivo, 'r') as archivo:
            # Leer todo el contenido del archivo
            contenido = archivo.read()
            # Imprimir el contenido del archivo
            print("El contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        # Manejar el caso en el que el archivo no se pueda encontrar
        print("No se pudo encontrar el archivo")

# Llamar a la función para escribir en un archivo
Escribir_archivo()

# Llamar a la función para leer un archivo
Leer_archivo()
