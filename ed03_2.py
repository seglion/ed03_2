"""
Este módulo procesa datos de entrada y genera un informe.
Autor: Miguel Angel Vigo
Fecha: 27/11/2024
"""

import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Configurar el logger
logger = logging.getLogger("CalculadoraCientifica")
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler("calculadora.log")
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class CalculadoraCientifica:
    """
    Esta clase representa una calculadora científica con funcionalidades avanzadas
    como operaciones trigonométricas, logaritmos y más.
    """

    def __init__(self):
        logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Se esperaba un número, se recibió {type(num)}")

    # Operaciones básicas
    def sumar(self, a, b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info("Sumando {%d} + {%d}", a, b)
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info("Restando %s - %s", a, b)
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info("Multiplicando  %s * %s", a, b)
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info("Dividiendo %s / %s", a, b)
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info("Calculando %s ^ %s", base, exponente)
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error(
                "Intento de calcular raíz cuadrada de número negativo: %s", numero
            )
            raise ValueError(
                "No se puede calcular la raíz cuadrada de un número negativo"
            )
        logger.info("Calculando raíz cuadrada de %s", numero)
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                "Intento de calcular logaritmo de número no positivo: %s", numero
            )
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero"
            )
        logger.info("Calculando logaritmo natural de %s", numero)
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                "Intento de calcular logaritmo base 10 de número no positivo: %s",
                numero,
            )
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero"
            )
        logger.info("Calculando logaritmo base 10 de %s", numero)
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando seno de %s radianes", angulo)
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando coseno de %s radianes", angulo)
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando tangente de %s radianes", angulo)
        return math.tan(angulo)


def main():
    """
    Función principal del programa.
    Ejecuta el flujo principal de la aplicación.
    """
    # Crear instancia de la calculadora
    calc = CalculadoraCientifica()
    try:
        # Ejemplos de uso de operaciones básicas
        print("\n=== Operaciones Básicas ===")
        print(f"Suma de 5 + 3 = {calc.sumar(5, 3)}")
        print(f"Resta de 10 - 4 = {calc.restar(10, 4)}")
        print(f"Multiplicación de 6 * 7 = {calc.multiplicar(6, 7)}")
        print(f"División de 15 / 3 = {calc.dividir(15, 3)}")
        # Ejemplos de uso de operaciones avanzadas
        print("\n=== Operaciones Avanzadas ===")
        print(f"Potencia de 2^3 = {calc.potencia(2, 3)}")
        print(f"Raíz cuadrada de 16 = {calc.raiz_cuadrada(16)}")
        print(f"Logaritmo natural de 2.718 = {calc.logaritmo_natural(2.718)}")
        print(f"Logaritmo base 10 de 100 = {calc.logaritmo_base_10(100)}")

        # Ejemplos de funciones trigonométricas
        print("\n=== Funciones Trigonométricas ===")
        angulo = math.pi / 2
        print(f"Seno de π/2 = {calc.seno(angulo)}")
        print(f"Coseno de π/2 = {calc.coseno(angulo)}")
        print(f"Tangente de π/4 = {calc.tangente(math.pi/4)}")

        # Ejemplo de manejo de errores
        print("\n=== Prueba de Manejo de Errores ===")
        print("Intentando dividir por cero:")
        calc.dividir(5, 0)

    except ValueError as e:
        logger.error("Error de valor: %s", str(e))
        print(f"Error de valor: {e}")
    except TypeError as e:
        logger.error("Error de tipo: %s", str(e))
        print(f"Error de tipo: {e}")
    except Exception as e:
        logger.error("Error inesperado: %s", str(e))
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
