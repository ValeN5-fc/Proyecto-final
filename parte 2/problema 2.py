import random # El modulo de aqui se usa paa genrar numeros aleatorios
def main():
    num = 0
    cont = 0
    # Esta funcion genera un numero aleatorio entre 1 y 100
    dato = random.randint(1, 100)

    print("\t\t¿Podrás adivinar el número?")

    # Aqui usamos un bucle para que el usuario intente adivinar el numero
    while num != dato:
        num = int(input("Digite el número: "))
        # Aqui indicamos al usuario si el numero que debe digitar es mayor o menor
        if num > dato:
            print("Digite un número menor")
        elif num < dato:
            print("Digite un número mayor")

        cont += 1 # Aqui aumentamos el contador por intento que realize el usuario

    print("¡Adivinó el número!")
    print(f"Número de intentos: {cont}")
    # Se veridica si se está ejecutando como el programa principal
if __name__ == "__main__":
    main()
