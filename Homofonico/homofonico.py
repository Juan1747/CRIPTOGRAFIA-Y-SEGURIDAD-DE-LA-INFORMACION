import random
import string

class HomophonicCipher:
    """
    Implementación de Cifrado Homofónico con m=100 y n=26
    """
    
    def __init__(self, use_class_layout=True):
        """
        Inicializa el cifrador con el layout especificado
        
        Args:
            use_class_layout: Si es True, usa el layout de la clase. 
                            Si es False, genera uno aleatorio.
        """
        self.m = 100  # Tamaño del alfabeto de cifrado (0-99)
        self.n = 26   # Tamaño del alfabeto de texto plano (A-Z)
        
        if use_class_layout:
            self.layout = self._create_class_layout()
        else:
            self.layout = self._create_random_layout()
        
        # Crear diccionario inverso para descifrado
        self.reverse_layout = self._create_reverse_layout()
    
    def _create_class_layout(self):
        """
        Crea el layout visto en clase basado en las frecuencias del español
        """
        layout = {
            'A': [9, 12, 23, 47, 53, 67, 73, 92],
            'B': [48, 61],
            'C': [13, 14, 62],
            'D': [1, 3, 45, 79],
            'E': [0, 11, 24, 44, 55, 57, 64, 74, 82, 87, 98],
            'F': [10, 31],
            'G': [6, 25],
            'H': [2, 56, 66, 68],
            'I': [32, 70, 75, 88, 93],
            'J': [15],
            'K': [4],
            'L': [29, 51, 84],
            'M': [26, 27],
            'N': [18, 35, 58, 71, 91],
            'O': [5, 7, 54, 72, 90, 99],
            'P': [8, 94],
            'Q': [41],
            'R': [40, 42, 77, 80],
            'S': [20, 36, 76, 86, 96],
            'T': [30, 33, 43, 46, 60, 85, 97],
            'U': [69],
            'V': [83],
            'W': [89],
            'X': [28],
            'Y': [21, 52],
            'Z': [16]
        }
        return layout
    
    def _create_random_layout(self):
        """
        Crea un layout aleatorio distribuyendo 100 números entre 26 letras
        basado en frecuencias aproximadas del español
        """
        # Frecuencias aproximadas en español
        frequencies = {
            'E': 12, 'A': 11, 'O': 9, 'S': 8, 'N': 7, 'R': 7,
            'I': 6, 'D': 6, 'L': 5, 'C': 5, 'T': 5, 'U': 4,
            'M': 3, 'P': 3, 'B': 2, 'G': 2, 'V': 2, 'Y': 2,
            'Q': 1, 'H': 1, 'F': 1, 'Z': 1, 'J': 1, 'Ñ': 1,
            'X': 1, 'W': 1, 'K': 1
        }
        
        # Ajustar para que sumen exactamente 100
        total = sum(frequencies.values())
        if total != 100:
            frequencies['E'] += (100 - total)
        
        # Crear lista de números disponibles
        numbers = list(range(100))
        random.shuffle(numbers)
        
        layout = {}
        index = 0
        
        for letter in string.ascii_uppercase:
            count = frequencies.get(letter, 1)
            layout[letter] = sorted(numbers[index:index + count])
            index += count
        
        return layout
    
    def _create_reverse_layout(self):
        """
        Crea el diccionario inverso para descifrado
        Mapea cada número de cifrado a su letra original
        """
        reverse = {}
        for letter, numbers in self.layout.items():
            for num in numbers:
                reverse[num] = letter
        return reverse
    
    def encrypt(self, plaintext):
        """
        Cifra un mensaje de texto plano
        
        Args:
            plaintext: Mensaje en texto claro
            
        Returns:
            Lista de números que representan el texto cifrado
        """
        plaintext = plaintext.upper().replace(' ', '')
        ciphertext = []
        
        for char in plaintext:
            if char in self.layout:
                # Elegir aleatoriamente uno de los números asignados a esta letra
                possible_numbers = self.layout[char]
                chosen_number = random.choice(possible_numbers)
                ciphertext.append(chosen_number)
            else:
                # Ignorar caracteres que no están en el alfabeto
                continue
        
        return ciphertext
    
    def decrypt(self, ciphertext):
        """
        Descifra un mensaje cifrado
        
        Args:
            ciphertext: Lista de números o string separado por espacios
            
        Returns:
            Texto plano descifrado
        """
        # Si el texto cifrado es un string, convertirlo a lista de enteros
        if isinstance(ciphertext, str):
            ciphertext = [int(x.strip()) for x in ciphertext.split()]
        
        plaintext = []
        
        for num in ciphertext:
            if num in self.reverse_layout:
                plaintext.append(self.reverse_layout[num])
            else:
                plaintext.append('?')  # Número no válido
        
        return ''.join(plaintext)
    
    def print_layout(self):
        """
        Imprime el layout completo
        """
        print("\n=== LAYOUT DEL CIFRADO HOMOFÓNICO ===")
        print(f"m = {self.m}, n = {self.n}\n")
        
        for letter in sorted(self.layout.keys()):
            numbers = sorted(self.layout[letter])
            print(f"{letter}: {numbers}")
        print()


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("   CIFRADO HOMOFÓNICO - m=100, n=26")
    print("=" * 60)
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Ver layout completo")
    print("4. Salir")
    print("=" * 60)

def main():
    # Crear instancia con layout de la clase
    cipher = HomophonicCipher(use_class_layout=True)
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            # Cifrar mensaje
            print("\n--- CIFRAR MENSAJE ---")
            mensaje = input("Ingrese el mensaje a cifrar: ").strip()
            
            if not mensaje:
                print("❌ Error: El mensaje no puede estar vacío")
                continue
            
            texto_cifrado = cipher.encrypt(mensaje)
            print(f"\n✅ Mensaje original: {mensaje}")
            print(f"✅ Texto cifrado: {' '.join(map(str, texto_cifrado))}")
            
        elif opcion == '2':
            # Descifrar mensaje
            print("\n--- DESCIFRAR MENSAJE ---")
            print("Ingrese los números separados por espacios")
            texto_cifrado = input("(ejemplo: 14 42 32 8 97): ").strip()
            
            if not texto_cifrado:
                print("❌ Error: Debe ingresar números")
                continue
            
            try:
                texto_descifrado = cipher.decrypt(texto_cifrado)
                print(f"\n✅ Texto cifrado: {texto_cifrado}")
                print(f"✅ Mensaje descifrado: {texto_descifrado}")
            except ValueError:
                print("❌ Error: Formato incorrecto. Use números separados por espacios")
            
        elif opcion == '3':
            # Ver layout
            cipher.print_layout()
            input("\nPresione Enter para continuar...")
            
        elif opcion == '4':
            # Salir
            print("\n¡Hasta luego! 👋")
            break
            
        else:
            print("❌ Opción no válida. Por favor seleccione 1-5")


if __name__ == "__main__":
    main()