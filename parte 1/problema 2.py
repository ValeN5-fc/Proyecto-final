# Definición de la función para invertir una cadena
def invertirCadena(cadena):
    # cadena[::-1] devuelve la cadena desde el último carácter hasta el primero, invirtiéndola.
    cadena_invertida = cadena[::-1]
    # Devolvemos la cadena invertida
    return cadena_invertida

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese la cadena a invertir: ")

# Llamar a la función para invertir la cadena
cadena_invertida = invertirCadena(cadena)

# Imprimir la cadena original y la cadena invertida
print("la cadena original: ", cadena)
print("la cadena invertida: ", cadena_invertida)
