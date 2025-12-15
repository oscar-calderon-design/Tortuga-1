# mini_turtle

Paquete funcional educativo que demuestra modularidad en Python: separa la **lógica interna y el estado** (`drawer_logic.py`) de la **interfaz pública** (`__init__.py`). Expone las funciones `adelante`, `abajo` y `reiniciar` para construir dibujos ASCII simples.

## ¿Cómo funciona?
- `posicion_x` es una variable global que representa la posición horizontal actual del "lápiz".
- `adelante(pasos)` imprime un tramo horizontal (`_`) y avanza `posicion_x`.
- `abajo(longitud)` imprime líneas verticales (`|`) alineadas con la `posicion_x` actual.
- `reiniciar()` pone `posicion_x = 0` para iniciar un nuevo dibujo desde el origen.
- `mini_turtle/__init__.py` reexporta las funciones para permitir `from mini_turtle import ...` sin exponer detalles internos.

## Estructura
```
mini_turtle_task/
├── mini_turtle/
│   ├── __init__.py       # Interfaz pública
│   └── drawer_logic.py   # Lógica y estado global
├── main.py               # Script de prueba
├── pyproject.toml        # Opcional para empaquetado
└── README.md
```

## Uso rápido (API)
```
from mini_turtle import adelante, abajo, reiniciar

adelante(4)
abajo(2)
reiniciar()
```

## Cómo ejecutarlo
1) Abre una consola en `C:\Users\Emilse \OneDrive\Documents\Tarea`.
2) Usa el lanzador de Python en Windows:
```
py -3 main.py
```
3) En Linux/Mac (si aplica):
```
python3 mini_turtle_task/main.py
```

Notas:
- No ejecutes `__init__.py` directamente: el paquete se usa **importando** o ejecutando `main.py`.
- Si la ventana de la terminal se cierra al terminar, abre la consola manualmente y ejecuta el comando anterior (o usa `powershell -NoExit -Command "py -3 mini_turtle_task\\main.py"`).

## Empaquetado (opcional)
- El archivo `pyproject.toml` permite construir el paquete con `setuptools`. Para un entorno local:
```
py -m pip install -e .
```
Ejecuta ese comando dentro de `mini_turtle_task` si deseas instalar el paquete editable.

## Imagenes

