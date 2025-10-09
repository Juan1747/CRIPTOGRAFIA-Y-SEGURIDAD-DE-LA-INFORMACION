# Algoritmos de Cifrado

Este repositorio contiene varios algoritmos de cifrado implementados en Python. A continuación se describen brevemente cada uno de los algoritmos:

## 1. Caesar.py
El **Cifrado César** es uno de los cifrados más antiguos. Funciona desplazando cada letra del texto por un número fijo de posiciones en el alfabeto. Es un algoritmo de sustitución simple, y aunque es fácil de implementar, es muy vulnerable a los ataques de fuerza bruta.

## 2. Hill.py
El **Cifrado de Hill** es un cifrado de sustitución polialfabético basado en matrices. Utiliza álgebra lineal y operaciones de matrices para cifrar el texto. Es más complejo que el Cifrado César y proporciona un nivel de seguridad más alto al utilizar una clave de matriz para realizar la sustitución.

## 3. OTP.py (One-Time Pad)
El **Cifrado de un solo uso (OTP)** es un algoritmo de cifrado que utiliza una clave completamente aleatoria, que debe ser tan larga como el mensaje. Cada bit del mensaje se combina con un bit de la clave mediante la operación XOR. Si la clave se utiliza una sola vez y es completamente aleatoria, este cifrado es teóricamente impenetrable.

## 4. Homofonico.py
El **Cifrado homofónico** es un tipo de cifrado de sustitución en el que una letra puede ser sustituida por varios símbolos diferentes. Esto mejora la seguridad frente a los ataques de análisis de frecuencia, ya que impide que se puedan hacer suposiciones sobre la frecuencia de aparición de las letras.

## 5. Play-fair.py
El **Cifrado Playfair** es un cifrado por sustitución digráfica que opera sobre pares de letras. La clave se utiliza para crear una matriz de 5x5, y el texto claro se divide en pares de letras. Si hay letras duplicadas en un par, se sustituyen por un carácter específico para mantener el formato del texto cifrado.

## 6. Turning_grille.py
El **Cifrado Turning Grille** es un cifrado de sustitución que utiliza una "rejilla" o "plantilla" con huecos que se giran para cifrar el texto. En cada paso, la rejilla permite que ciertas letras del texto sean vistas y reemplazadas por otras en un patrón que cambia con cada giro de la rejilla.

## 7. Vigenere.py
El **Cifrado Vigenère** es un cifrado de sustitución polialfabético que utiliza una clave repetida para cifrar el texto. A diferencia del Cifrado César, la clave no es fija, lo que hace que este algoritmo sea mucho más difícil de romper. Es especialmente vulnerable a los ataques de análisis de frecuencia si la longitud de la clave es pequeña.

---

## Requisitos
Para ejecutar los algoritmos de cifrado, necesitas tener Python instalado en tu sistema.

```bash
pip install -r requirements.txt
