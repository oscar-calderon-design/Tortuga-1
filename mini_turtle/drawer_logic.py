"""Lógica interna del paquete mini_turtle.

Contiene el estado global y las funciones de dibujo ASCII. Este módulo NO es
la interfaz pública; se consume a través de `mini_turtle.__init__`.
"""

# Estado global: posición horizontal actual del "lápiz" en el lienzo ASCII
posicion_x: int = 0

def adelante(pasos: int = 1) -> int:
    """Dibuja un tramo horizontal y avanza la posición.

    pasos: cantidad de caracteres "_" a imprimir (debe ser >= 0)
    return: nueva posición horizontal tras avanzar
    """
    global posicion_x  # Usamos la variable global porque vamos a modificarla
    if pasos < 0:
        # Validación defensiva: no permitir valores negativos
        raise ValueError("pasos debe ser no negativo")
    inicio = posicion_x  # Guardamos dónde empezamos para alinear la salida
    # Imprime espacios para alinear y luego el tramo horizontal
    print(" " * inicio + "_" * pasos)
    # Avanza la posición para próximos trazos
    posicion_x += pasos
    # Devuelve la posición actualizada por si se desea consultar
    return posicion_x

def abajo(longitud: int = 1) -> int:
    """Dibuja líneas verticales alineadas con la posición actual.

    longitud: número de líneas "|" a imprimir (debe ser >= 0)
    return: posición horizontal (no cambia al bajar)
    """
    global posicion_x  # Leemos la posición para alinear las líneas
    if longitud < 0:
        raise ValueError("longitud debe ser no negativa")
    # Imprime tantas líneas como indique 'longitud'
    for _ in range(longitud):
        print(" " * posicion_x + "|")
    return posicion_x

def reiniciar() -> None:
    """Restablece la posición horizontal al inicio (0)."""
    global posicion_x  # Indicamos que vamos a asignar a la global
    posicion_x = 0