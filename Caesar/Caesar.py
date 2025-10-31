# ===== Diccionario =====
arr_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z']

dicc = {letra: i for i, letra in enumerate(arr_)}   # letra -> número
inv = {i: letra for letra, i in dicc.items()}        # número -> letra

# ===== Entradas =====
action = input("¿Quieres cifrar (1) o descifrar (0)?: ").strip()

# Validación de action
if action not in ("1", "0"):
    print("Opción inválida. Usa '1' para cifrar o '0' para descifrar.")
    exit(1)

action = int(action)  # lo convertimos a número

message = input("Mensaje: ").strip().lower()
k = int(input("Parámetro k (desplazamiento): "))

# ===== Proceso =====
resultado = []

for letter in message:
    if letter not in dicc:   # ignorar caracteres que no son letras
        resultado.append(letter)
        continue

    pos = dicc[letter]

    if action == 1:  # Cifrar
        nueva_pos = (pos + k) % 26
        resultado.append(inv[nueva_pos])

    elif action == 0:  # Descifrar
        nueva_pos = (pos - k) % 26
        resultado.append(inv[nueva_pos])

# ===== Salida =====
texto_final = "".join(resultado)
print("Resultado:", texto_final)
