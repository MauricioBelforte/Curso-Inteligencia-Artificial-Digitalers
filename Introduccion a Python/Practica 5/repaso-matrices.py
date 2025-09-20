
# Una lista se llama Matriz cuando contiene otras listas como elementos
m = [[2,3],[5,6]]



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# En este ejemplo, el for fila in matriz: se da cuenta que la matriz tiene filas porque Python interpreta cada elemento dentro de la lista principal (matriz) como una sublista, y las recorre una por una.


# Recorrer e imprimir la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea después de cada fila