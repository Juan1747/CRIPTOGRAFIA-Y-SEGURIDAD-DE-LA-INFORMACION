# Cifra y descifra una imagen con AES (CTR) usando pyaes.
# Requisitos del taller:
# - Recibe una imagen (cualquier formato).
# - Cifra con AES y nivel 128/192/256 bits como parámetro CLI.
# - Codifica cifrado en Base64, lo muestra en consola.
# - Decodifica Base64, descifra, genera imagen original y la muestra.

import argparse
import base64
import os
import sys
from typing import Tuple

import matplotlib.pyplot as plt
from skimage import io

import pyaes  # pip install pyaes


def read_file_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def write_file_bytes(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)


def split_ext(path: str) -> Tuple[str, str]:
    name, ext = os.path.splitext(path)
    return name, ext.lstrip(".")


def encrypt_aes_ctr(key: bytes, plaintext: bytes) -> bytes:
    """
    Para poder descifrar correctamente en otra instancia, incluimos un 'nonce'
    de 8 bytes al inicio del mensaje (antes del ciphertext). El contador CTR se
    inicializa con ese nonce.
    Estructura: [8 bytes NONCE] + [CIPHERTEXT]
    """
    nonce = os.urandom(8)
    initial_value = int.from_bytes(nonce, "big")
    ctr = pyaes.Counter(initial_value)
    aes = pyaes.AESModeOfOperationCTR(key, ctr)
    ciphertext = aes.encrypt(plaintext)
    return nonce + ciphertext


def decrypt_aes_ctr(key: bytes, msg: bytes) -> bytes:
    """
    Espera el formato [NONCE(8)][CIPHERTEXT].
    """
    if len(msg) < 8:
        raise ValueError("Mensaje inválido: no contiene NONCE.")
    nonce = msg[:8]
    ciphertext = msg[8:]
    initial_value = int.from_bytes(nonce, "big")
    ctr = pyaes.Counter(initial_value)
    aes = pyaes.AESModeOfOperationCTR(key, ctr)
    return aes.decrypt(ciphertext)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Cifrar/descifrar una imagen con AES (CTR) y mostrar Base64."
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Ruta a la imagen de entrada (jpg, png, etc.)"
    )
    parser.add_argument(
        "--bits",
        "-b",
        type=int,
        choices=[128, 192, 256],
        required=True,
        help="Nivel de seguridad: 128, 192 o 256 bits.",
    )
    parser.add_argument(
        "--keyhex",
        help="Clave en HEX opcional (32/48/64 hex-chars para 128/192/256 bits). Si no se provee, se genera aleatoria.",
    )
    parser.add_argument(
        "--save-b64",
        help="(Opcional) Ruta de salida para guardar también el Base64 (txt).",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="No mostrar las imágenes con matplotlib (útil en ejecución headless).",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # 1) Validar input
    in_path = args.input
    if not os.path.isfile(in_path):
        print(f"ERROR: No se encontró el archivo: {in_path}")
        sys.exit(1)

    # 2) Preparar clave
    nbytes = {128: 16, 192: 24, 256: 32}[args.bits]
    if args.keyhex:
        try:
            key = bytes.fromhex(args.keyhex)
        except ValueError:
            print("ERROR: keyhex no es hex válido.")
            sys.exit(1)
        if len(key) != nbytes:
            print(f"ERROR: keyhex debe tener {nbytes*2} caracteres hex para {args.bits} bits.")
            sys.exit(1)
        key_source = "proporcionada (HEX)"
    else:
        key = os.urandom(nbytes)
        key_source = "generada aleatoriamente"

    print("**** AES (Advanced Encryption Standard) - Modo CTR ****")
    print(f"Nivel: {args.bits} bits")
    print(f"Clave ({key_source}): {key.hex()}")

    # 3) Leer bytes de la imagen
    plain = read_file_bytes(in_path)

    # 4) Cifrar (CTR con nonce explícito)
    msg = encrypt_aes_ctr(key, plain)

    # 5) Codificar en Base64 y mostrar en consola
    b64 = base64.b64encode(msg).decode("ascii")
    print("\n--- MENSAJE CIFRADO EN BASE64 ---")
    print(b64)

    if args.save_b64:
        write_file_bytes(args.save_b64, b64.encode("utf-8"))
        print(f"(Guardado Base64 en: {args.save_b64})")

    # 6) Decodificar desde Base64 a bytes
    msg_from_b64 = base64.b64decode(b64)

    # 7) Descifrar
    recovered = decrypt_aes_ctr(key, msg_from_b64)

    # 8) Escribir imagen recuperada y mostrar
    _, ext = split_ext(in_path)
    out_path = f"decrypted_image.{ext if ext else 'bin'}"
    write_file_bytes(out_path, recovered)
    print(f"\nImagen descifrada guardada como: {out_path}")

    if not args.no_show:
        try:
            original_img = io.imread(in_path)
            rec_img = io.imread(out_path)

            plt.figure()
            plt.title(f"Original: {os.path.basename(in_path)}")
            plt.axis("off")
            plt.imshow(original_img)

            plt.figure()
            plt.title(f"Recuperada: {os.path.basename(out_path)}")
            plt.axis("off")
            plt.imshow(rec_img)

            plt.show()
        except Exception as e:
            print(f"Nota: no se pudieron mostrar las imágenes. Detalle: {e}")


if __name__ == "__main__":
    main()
