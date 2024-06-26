def suma(a, b): # Funcion para sumar dos numeros
    return a + b
def resta(a, b): # Funcion para restar dos numeros
    return a - b
def multiplicacion(a, b): # Funcion para multiplicar dos numeros
    return a * b
def division(a, b): # Funcion para dividir dos numeros
    if b != 0:
        return a / b
    else:
        return "Indeterminada"
def main():
    opcion = 0
    while opcion <= 0 or opcion > 5:
        print("\t\tBienvenido a la calculadora: ") # Menu interactivo para saber que funcion desea el usuario ingresar
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        print("Digite una operacion: ")
        opcion = int(input())
    if opcion == 5:  # Aqui por si no desea usar la calculadora
        print("Gracias por usar la calculadora")
        return
    num1 = float(input("Digite el primer numero: "))# Digitamos los 2 numeros para usar las respectivas funciones
    num2 = float(input("Digite el segundo numero: "))
    # Aqui se ejecuta las funciones segun corresponda
    if opcion == 1:
        print(f"La suma de los numeros es: {suma(num1, num2)}")
    elif opcion == 2:
        print(f"La resta de los numeros es: {resta(num1, num2)}")
    elif opcion == 3:
        print(f"La multiplicacion de los numeros es: {multiplicacion(num1, num2)}")
    elif opcion == 4:
        resultado_division = division(num1, num2)
        print(f"La division de los numeros es: {resultado_division}")
# Se veridica si se está ejecutando como el programa principal
if __name__ == "__main__":
    main()
