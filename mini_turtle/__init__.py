"""Interfaz pública del paquete mini_turtle.

Permite importar directamente `adelante`, `abajo` y `reiniciar` sin conocer
la ubicación interna de la lógica.
"""

# Importación relativa: trae las funciones desde el módulo interno del paquete
from .drawer_logic import adelante, abajo, reiniciar

# Controla qué nombres se exportan si se usa `from mini_turtle import *`
__all__ = ["adelante", "abajo", "reiniciar"]