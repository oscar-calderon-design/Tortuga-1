"""Script de prueba para el paquete mini_turtle.

Demuestra cómo usar las funciones públicas del paquete para dibujar figuras
ASCII y cómo reiniciar el estado para comenzar un nuevo dibujo.
"""

# Importamos la API pública del paquete: no necesitamos conocer la lógica interna
from mini_turtle import adelante, abajo, reiniciar

# Primera figura: una escalera de 5 escalones
print("Escalera 1:")
for _ in range(5):
    # Tramo horizontal de 4 caracteres, avanzando la posición
    adelante(4)
    # Dos líneas verticales, alineadas con la posición actual
    abajo(2)

# Reiniciamos la posición para empezar un nuevo dibujo desde el origen
print("\nReinicio:")
reiniciar()
print("posicion_x reiniciada a 0")

# Segunda figura: un tramo más largo y líneas verticales
print("\nFigura 2:")
adelante(5)
abajo(3)