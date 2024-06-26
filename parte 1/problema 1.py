# Definición de la función factorial
def factorial(numero):
    # Caso base: si el número es 0, el factorial es 1
    if numero == 0:
        return 1
    else:
        # Llamada recursiva: calcula el factorial del número restando 1
        # y multiplicándolo por el factorial del número anterior
        return numero * factorial(numero - 1)

# Solicitar al usuario que ingrese un número para calcular su factorial
numero = int(input("Digite un numero para hallar su factorial: "))

# Calcular el factorial del número ingresado llamando a la función factorial
resultado = factorial(numero)

# Imprimir el resultado del cálculo del factorial
print("El factorial de", numero, "es:", resultado)
