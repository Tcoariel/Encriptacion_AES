def mix_columns(state):
    filas = 4
    columnas = 4

    matriz1 = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    matriz2 = state

    matrizC = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            suma = 0
            for k in range(filas):
                suma += matriz1[i][k] * matriz2[k][j]
            matrizC[i][j] = suma % 256  
    
    return matrizC
