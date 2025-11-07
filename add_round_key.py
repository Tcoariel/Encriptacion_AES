def add_round_key(matriz_texto, matriz_clave):
    nueva_matriz = []
    for i in range(4):
        fila = []
        for j in range(4):
            valor = matriz_texto[i][j] ^ matriz_clave[i][j]  
            fila.append(valor)
        nueva_matriz.append(fila)
    return nueva_matriz
