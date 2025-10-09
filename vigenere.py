#-------------------------Vigenere cypher-----------------------------------
import argparse
import unicodedata
import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A2I = {c:i for i,c in enumerate(ALPHABET)}
I2A = {i:c for i,c in enumerate(ALPHABET)}

def strip_accents(s: str) -> str:
    # Normalize accents to plain ASCII
    return ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn')

def normalize_letters(s: str) -> str:
    s = strip_accents(s).upper()
    return ''.join(ch for ch in s if ch.isalpha())

def repeat_key(key: str, n: int) -> str:
    if n == 0:
        return ''
    key = normalize_letters(key)
    if not key:
        raise ValueError("Key must contain at least one alphabetic character.")
    times = (n // len(key)) + 1
    return (key * times)[:n]

def vigenere_encrypt(plaintext: str, key: str) -> str:
    P = normalize_letters(plaintext)
    K = repeat_key(key, len(P))
    out = []
    for p, k in zip(P, K):
        c = (A2I[p] + A2I[k]) % 26
        out.append(I2A[c])
    return ''.join(out)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    C = normalize_letters(ciphertext)
    K = repeat_key(key, len(C))
    out = []
    for c, k in zip(C, K):
        p = (A2I[c] - A2I[k]) % 26
        out.append(I2A[p])
    return ''.join(out)

def chunk_group(s: str, t: int) -> str:
    if t <= 0:
        return s
    return ' '.join(s[i:i+t] for i in range(0, len(s), t))

def main():
    parser = argparse.ArgumentParser(description="Vigenère cipher")
    sub = parser.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--key", "-k", required=True, help="Keyword (letters only; accents/spaces ignored)")
    common.add_argument("--t", "-t", type=int, required=True, help="Block size for formatting (does not affect the cipher)")
    common.add_argument("--text", "-x", required=True, help="Input text (message for encrypt, ciphertext for decrypt)")

    p_enc = sub.add_parser("encrypt", parents=[common], help="Encrypt plaintext")
    p_dec = sub.add_parser("decrypt", parents=[common], help="Decrypt ciphertext")

    args = parser.parse_args()

    try:
        if args.cmd == "encrypt":
            cipher = vigenere_encrypt(args.text, args.key)
            print("Mode       : ENCRYPT")
            print("Key        :", normalize_letters(args.key))
            print("t (blocks) :", args.t)
            print("Plaintext  :", chunk_group(normalize_letters(args.text), args.t))
            print("Ciphertext :", chunk_group(cipher, args.t))
        else:
            plain = vigenere_decrypt(args.text, args.key)
            print("Mode       : DECRYPT")
            print("Key        :", normalize_letters(args.key))
            print("t (blocks) :", args.t)
            print("Ciphertext :", chunk_group(normalize_letters(args.text), args.t))
            print("Plaintext  :", chunk_group(plain, args.t))
    except ValueError as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
