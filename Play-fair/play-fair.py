# ===== Funciones =====

def make_pairs(message):
    message = message.replace("j", "i")  # normalizar
    pairs = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i+1]
            if a == b:  # si son iguales, insertar 'x'
                pairs.append(a + "x")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:  # última letra sola
            pairs.append(a + "x")
            i += 1
    return pairs

def find_position(matrix, letter):
    if letter == "j":  # normalizamos j -> i
        letter = "i"
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# ===== Entrada =====
action = input("¿Quieres cifrar (1) o descifrar (0)?: ").strip()


if action not in ("1", "0"):
    print("Opción inválida. Usa '1' para cifrar o '0' para descifrar.")
    exit(1)

action = int(action)  # convertir a número

message = input("Mensaje: ").strip().lower().replace(" ", "")
key = input("Llave: ").strip().lower()


message = ''.join(ch for ch in message if ch.isalpha())

# alfabeto sin 'j' 
arr_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']

# inicializar matriz vacía
matrix = [[None for _ in range(5)] for _ in range(5)]

arr_letters = []
cont = 0

# Normalizar la key (reemplazar j -> i)
key = key.replace("j", "i")

# Insertar las letras de la key
for letter in key:
    if letter not in arr_letters and letter in arr_:
        row = cont // 5
        col = cont % 5
        matrix[row][col] = letter
        arr_letters.append(letter)
        cont += 1

# Rellenar con el resto del alfabeto
for letter in arr_:
    if letter not in arr_letters:
        row = cont // 5
        col = cont % 5
        matrix[row][col] = letter
        arr_letters.append(letter)
        cont += 1
        if cont >= 25:
            break

# Mostrar la matriz Playfair
print("\nMatriz Playfair:")
for fila in matrix:
    print(fila)

# ===== Procesar mensaje =====
message_pairs = make_pairs(message)
resultado = []

for pair in message_pairs:
    a, b = pair[0], pair[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if action == 1:  # Cifrar
        if row_a == row_b:  # misma fila → derecha
            resultado.append(matrix[row_a][(col_a + 1) % 5])
            resultado.append(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:  # misma columna → abajo
            resultado.append(matrix[(row_a + 1) % 5][col_a])
            resultado.append(matrix[(row_b + 1) % 5][col_b])
        else:  # rectángulo
            resultado.append(matrix[row_a][col_b])
            resultado.append(matrix[row_b][col_a])

    elif action == 0:  # Descifrar
        if row_a == row_b:  # misma fila → izquierda
            resultado.append(matrix[row_a][(col_a - 1) % 5])
            resultado.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:  # misma columna → arriba
            resultado.append(matrix[(row_a - 1) % 5][col_a])
            resultado.append(matrix[(row_b - 1) % 5][col_b])
        else:  # rectángulo
            resultado.append(matrix[row_a][col_b])
            resultado.append(matrix[row_b][col_a])

# ===== Salida final =====
texto_final = "".join(resultado)
print("\nResultado:", texto_final)
