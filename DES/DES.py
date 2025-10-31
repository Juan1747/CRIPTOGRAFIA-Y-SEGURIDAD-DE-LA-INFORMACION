# DES (pyDes) demo: cifra una imagen, la imprime en Base64, la descifra y la muestra.

import base64
import os
from pyDes import des, CBC, PAD_PKCS5
import matplotlib.pyplot as plt
from skimage import io

def main():
    print("**** DES (Data Encryption Standard) ****\n")

    # 1) Pedir ruta del archivo
    im = input("Introduzca el nombre del archivo con su extensión (por ej. foto.png): ").strip()
    if not os.path.isfile(im):
        print(f"ERROR: No se encontró el archivo: {im}")
        return

    # 2) Separar nombre y extensión de forma robusta
    sname, ext = os.path.splitext(im)
    ext = ext.lstrip(".")  # quitar el punto inicial

    # 3) Leer bytes del archivo en binario
    with open(im, "rb") as f:
        image_bytes = f.read()

    # 4) Configurar DES: clave de 8 bytes e IV de 8 bytes
    #    ¡OJO! DES es inseguro; esto es solo para demostración.
    key_bytes = b"KEYSANTI"                 # 8 bytes exactos
    iv_bytes = b"\x00\x00\x00\x00\x00\x00\x00\x00"  # IV nulo (8 bytes)

    cipher = des(key_bytes, CBC, iv_bytes, pad=None, padmode=PAD_PKCS5)

    # 5) Cifrar
    data_encrypted = cipher.encrypt(image_bytes)

    # 6) Mostrar en Base64
    b64 = base64.b64encode(data_encrypted).decode("ascii")
    print("Mensaje cifrado en Base64:")
    print(b64)

    # 7) (Opcional) simular recibir Base64 y decodificar
    not_b64 = base64.b64decode(b64)

    # 8) Descifrar
    data_decrypted = cipher.decrypt(not_b64)

    # 9) Guardar imagen descifrada
    out_name = f"decrypted_image.{ext if ext else 'bin'}"
    with open(out_name, "wb") as out:
        out.write(data_decrypted)

    print(f"\nImagen descifrada guardada como: {out_name}")

    # 10) Mostrar imagen con skimage + matplotlib si es realmente imagen
    try:
        new_image = io.imread(out_name)
        plt.title(f"Vista previa: {out_name}")
        plt.axis("off")
        plt.imshow(new_image)
        plt.show()
    except Exception as e:
        print(f"Nota: No se pudo mostrar como imagen (¿quizá no es un formato de imagen válido?). Detalle: {e}")

if __name__ == "__main__":
    main()
