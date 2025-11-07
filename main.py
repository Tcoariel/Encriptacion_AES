from substitute_bytes import substitute_bytes
from shift_rows import shift_rows
from mix_columns import mix_columns
from add_round_key import add_round_key


def texto_a_matriz(texto):
    bytes_texto = [ord(c) for c in texto]

    while len(bytes_texto) < 16:
        bytes_texto.append(0)

    matriz = [[0]*4 for _ in range(4)]
    idx = 0
    for col in range(4):
        for fila in range(4):
            matriz[fila][col] = bytes_texto[idx]
            idx += 1
    return matriz


def imprimir_matriz(matriz, titulo=""):
    if titulo:
        print(f"\n{titulo}")
    for fila in matriz:
        print(" ".join(f"{x:02x}" for x in fila))

def main():
    mensaje = input("Ingresa el mensaje (máx 16 caracteres): ")

    matriz_clave = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    state = texto_a_matriz(mensaje)
    imprimir_matriz(state, "Estado inicial (texto en bytes):")

    state = substitute_bytes(state)
    imprimir_matriz(state, "Después de Substitute Bytes:")

    state = shift_rows(state)
    imprimir_matriz(state, "Después de Shift Rows:")

    state = mix_columns(state)
    imprimir_matriz(state, "Después de Mix Columns:")

    state = add_round_key(state, matriz_clave)
    imprimir_matriz(state, "Después de Add Round Key (resultado final):")


if __name__ == "__main__":
    main()
