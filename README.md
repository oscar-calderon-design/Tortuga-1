# Mini Turtle - Dibujo ASCII Modular

Este proyecto es un paquete educativo escrito en Python que simula una "tortuga" de dibujo simple mediante arte ASCII en la consola. Su objetivo principal es demostrar conceptos de **modularidad**, separando claramente la lógica interna y el estado de la interfaz pública disponible para el usuario.

## 📝 Descripción

El programa permite dibujar figuras simples (como escaleras) en la terminal utilizando caracteres (`_` para trazos horizontales y `|` para verticales). Mantiene un estado interno de la posición horizontal ("x") del cursor, permitiendo que las siguientes líneas se dibujen alineadas correctamente con el final del trazo anterior.

El diseño del código sigue el principio de encapsulamiento:
*   **Lógica Interna**: Manejada en `drawer_logic.py`, donde reside la variable global de estado.
*   **Interfaz Pública**: Expuesta a través de `__init__.py`, permitiendo importar solo lo necesario (`adelante`, `abajo`, `reiniciar`).

## 📂 Estructura del Proyecto

```text
.
├── main.py               # Script principal de prueba y demostración
├── pyproject.toml        # Archivo de configuración del proyecto
├── README.md             # Documentación del proyecto
└── mini_turtle/          # Paquete principal
    ├── __init__.py       # Interfaz pública del paquete
    └── drawer_logic.py   # Implementación de la lógica y estado
```

## ⚙️ ¿Cómo funciona?

El sistema funciona manipulando una posición horizontal global (`posicion_x`).

1.  **`adelante(pasos)`**: Imprime una línea horizontal (`_`) de la longitud especificada y avanza la `posicion_x` esa misma cantidad.
2.  **`abajo(longitud)`**: Imprime líneas verticales (`|`) hacia abajo. Las líneas se indentan con espacios según la `posicion_x` actual para alinearse con el último punto horizontal.
3.  **`reiniciar()`**: Restablece la `posicion_x` a 0, permitiendo comenzar un nuevo dibujo desde el margen izquierdo sin reiniciar el programa.

## 🚀 Cómo ejecutarlo

### Requisitos
*   Tener instalado **Python 3**.

### Pasos para ejecutar
1.  Abre tu terminal o línea de comandos (CMD, PowerShell, Bash).
2.  Navega hasta la carpeta del proyecto donde se encuentra el archivo `main.py`.
3.  Ejecuta el siguiente comando según tu sistema operativo:

    **En Windows:**
    ```bash
    py main.py
    # O si tienes python en el PATH:
    python main.py
    ```

    **En macOS / Linux:**
    ```bash
    python3 main.py
    ```

## 💻 Ejemplo de Uso

Puedes usar las funciones importándolas desde el paquete `mini_turtle`:

```python
from mini_turtle import adelante, abajo, reiniciar

# Dibujar algo
adelante(4)
abajo(2)

# Reiniciar para un nuevo dibujo
reiniciar()
```

Al ejecutar `main.py`, verás una demostración automática generando escaleras y figuras.

## Imagenes

