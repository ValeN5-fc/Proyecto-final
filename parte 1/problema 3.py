# Creamos una lista vacía para almacenar elementos
lista = []
# Iniciamos un bucle while que se ejecutará indefinidamente hasta que se rompa explícitamente
while True:
    # Solicitamos al usuario que ingrese un elemento
    elemento = input("Ingrese un elemento (o 'salir' para finalizar): ")    
    # Verificamos si el usuario ingresó 'salir', en cuyo caso rompemos el bucle
    if elemento.lower() == 'salir':
        break    
    # Agregamos el elemento ingresado por el usuario a la lista
    lista.append(elemento) 
    # Imprimimos un mensaje para confirmar que el elemento se ha agregado correctamente a la lista
    print("El elemento se agrego correctamente a la Lista")
# Una vez que el usuario haya ingresado 'salir' y el bucle se haya roto, imprimimos los elementos de la lista
print("La lista contiene los siguientes elementos: ")
print(lista)
# Calculamos la cantidad de elementos en la lista utilizando la función len()
cantidad = len(lista)
# Imprimimos el tamaño de la lista
print("El tamanio de la lista es: ")
print(cantidad)
