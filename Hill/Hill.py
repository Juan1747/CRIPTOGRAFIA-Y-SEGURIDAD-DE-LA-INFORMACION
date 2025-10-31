import numpy as np
from math import gcd

# --- FUNCIONES MATEMÁTICAS Y DE VALIDACIÓN ---

def determinante(matriz):
    """Calcula el determinante de una matriz 2x2 bajo módulo 26."""
    return (matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]) % 26

def inverso_modular(a, m=26):
    """Encuentra el inverso modular de 'a' en módulo 'm'."""
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def verificar_inversa(matriz):
    """Verifica si el determinante es coprimo con 26."""
    det = determinante(matriz)
    return gcd(det, 26) == 1

# --- FUNCIONES DE CIFRADO Y DESCIFRADO ---

def hill_cifrado(mensaje, clave):
    """Cifra un mensaje usando el algoritmo de Hill con una clave 2x2."""
    mensaje = mensaje.lower().replace(" ", "")
    if len(mensaje) % 2 != 0:
        mensaje += 'x'
    
    mensaje_numeros = [ord(caracter) - ord('a') for caracter in mensaje]
    mensaje_matriz = np.array(mensaje_numeros).reshape(-1, 2).T
    
    cifrado_matriz = np.dot(clave, mensaje_matriz) % 26
    
    texto_cifrado = ''.join(chr(num + ord('a')) for num in cifrado_matriz.T.flatten())
    
    return texto_cifrado

def hill_descifrado(mensaje_cifrado, clave):
    """Descifra un mensaje usando el algoritmo de Hill con una clave 2x2."""
    det = determinante(clave)
    inv_det = inverso_modular(det)
    adjunta = np.array([[clave[1][1], -clave[0][1]], [-clave[1][0], clave[0][0]]])
    clave_inversa = (inv_det * adjunta) % 26
    
    mensaje_cifrado = mensaje_cifrado.lower().replace(" ", "")
    mensaje_numeros = [ord(caracter) - ord('a') for caracter in mensaje_cifrado]
    mensaje_matriz = np.array(mensaje_numeros).reshape(-1, 2).T
    
    descifrado_matriz = np.dot(clave_inversa, mensaje_matriz) % 26
    
   
    texto_descifrado = ''.join(chr(int(round(num)) + ord('a')) for num in descifrado_matriz.T.flatten())
    
    return texto_descifrado

# --- FUNCIÓN PRINCIPAL ---

def main():
    """Función principal que maneja la interacción con el usuario."""
    print("--- Cifrado de Hill (Matriz 2x2) ---")
    print("Primero, ingrese los 4 números de la matriz clave:")
    
    try:
        k11 = int(input("Valor de la fila 1, columna 1: "))
        k12 = int(input("Valor de la fila 1, columna 2: "))
        k21 = int(input("Valor de la fila 2, columna 1: "))
        k22 = int(input("Valor de la fila 2, columna 2: "))
        
        clave = np.array([[k11, k12], [k21, k22]])
    except ValueError:
        print("\nError: Ingrese solo números enteros para la clave.")
        return

    if not verificar_inversa(clave):
        print(f"\nError: La matriz de clave {clave.tolist()} no es válida.")
        print("Su determinante no es coprimo con 26 y no tiene inversa modular.")
        return
    
    print(f"\nMatriz de clave válida: {clave.tolist()}")

    opcion = input("Ingrese 'c' para cifrar o 'd' para descifrar: ").lower()
    
    if opcion == 'c':
        mensaje = input("Ingrese el mensaje a cifrar: ")
        mensaje_cifrado = hill_cifrado(mensaje, clave)
        print("\nMensaje cifrado:", mensaje_cifrado)
    
    elif opcion == 'd':
        mensaje_cifrado = input("Ingrese el mensaje a descifrar: ")
        mensaje_descifrado = hill_descifrado(mensaje_cifrado, clave)
        print("\nMensaje descifrado:", mensaje_descifrado)
    
    else:
        print("Opción no válida. Por favor, reinicie el programa.")

if __name__ == "__main__":
    main()