# ----------------------------Implementación del cifrado One-Time Pad (OTP)---------------------------

import random

# Función para convertir el mensaje a binario (ASCII)
def texto_a_binario(mensaje):
    return ''.join(format(ord(c), '08b') for c in mensaje)

# Función para obtener la longitud del mensaje en binario
def obtener_longitud_binario(mensaje):
    return len(texto_a_binario(mensaje))

# Función para generar la llave aleatoria
def generar_llave(longitud):
    return ''.join(random.choice(['0', '1']) for _ in range(longitud))

# Función para cifrar el mensaje usando XOR
def cifrar(mensaje_binario, llave):
    return ''.join(str(int(m) ^ int(k)) for m, k in zip(mensaje_binario, llave))

# Función para descifrar el mensaje usando XOR
def descifrar(mensaje_cifrado, llave):
    return ''.join(str(int(m) ^ int(k)) for m, k in zip(mensaje_cifrado, llave))

# Validacion del algoritmo
mensaje = "One Time Pad"
mensaje_binario = texto_a_binario(mensaje)  
longitud_binario = obtener_longitud_binario(mensaje)  
llave = generar_llave(longitud_binario)  

# Cifrar el mensaje
mensaje_cifrado = cifrar(mensaje_binario, llave)

# Descifrar el mensaje
mensaje_descifrado_binario = descifrar(mensaje_cifrado, llave)
# Convertir el mensaje descifrado a texto 
mensaje_descifrado = ''.join(chr(int(mensaje_descifrado_binario[i:i+8], 2)) for i in range(0, len(mensaje_descifrado_binario), 8))

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
print(f"llave: {llave}")
print(f"Mensaje descifrado: {mensaje_descifrado}")
