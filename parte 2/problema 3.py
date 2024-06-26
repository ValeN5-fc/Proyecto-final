def dolares(a):
    tasa_dolares = 0.26295 # Tasa de cambio  de soles a dólares
    cant_dolares = a * tasa_dolares # Convertir la cantidad de soles a dólares
    return cant_dolares
def euros(a):
    tasa_euros = 0.24488 # Tasa de cambio de soles a euros
    cant_euros = a * tasa_euros # Convertir la cantidad de soles a euros
    return cant_euros
def yenes(a):
    tasa_yenes = 41.91467 # Tasa de cambio de soles a yenes
    cant_yenes = a * tasa_yenes # Convertir la cantidad de soles a yenes
    return cant_yenes
def peso_mexicano(a):
    tasa_pesos = 4.71028 # Tasa de cambio de soles a pesos mexicanos
    cant_pesos = a * tasa_pesos # Convertir la cantidad de soles a pesos mexicanos
    return cant_pesos
def main():
    moneda = 0
    # Aqui usamos un bucle para que ingrese una cantidad de dinero real
    while True:
        moneda = float(input("Digite su cantidad de dinero en soles: "))
        if moneda >= 0:
            break
        # Aqui imprimimos el resultado de convertir nuestra cantidad de soles
        # a otras divisas precisando los 2 primeros decimales
    print("Las cantidades en otras divisas son:")
    print(f"En dólares: {dolares(moneda):.2f}")
    print(f"En euros: {euros(moneda):.2f}")
    print(f"En yenes: {yenes(moneda):.2f}")
    print(f"En pesos mexicanos: {peso_mexicano(moneda):.2f}")

# Se veridica si se está ejecutando como el programa principal
if __name__ == "__main__":
    main()
