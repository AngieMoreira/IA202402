def busqueda_lineal(lista, objetivo):
    # Recorrer la lista elemento por elemento
    for indice in range(len(lista)):
        # Si encontramos el objetivo, devolvemos el índice
        if lista[indice] == objetivo:
            return indice
    # Si no se encuentra el objetivo, devolvemos -1
    return -1

# Ejemplo de uso
lista = [4, 2, 9, 7, 5, 6]
objetivo = 7

resultado = busqueda_lineal(lista, objetivo)

print(f'El resultado es:{resultado}')

