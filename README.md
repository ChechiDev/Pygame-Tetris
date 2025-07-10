![Work in Progress](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)
# Python Tetris

Este proyecto ha sido desarrollado como ejercicio de lógica y programación modular.
El objetivo es implementar la lógica del juego Tetris en Python usando Pygame, con una estructura totalmente modular y escalable.

## Estructura del Proyecto

```
Pygame-Tetris/
│
├── main.py                # Punto de entrada del juego
├── cfg/
│   └── config.py          # Configuración global (tamaños, colores, etc.)
└── core/
    ├── __init__.py        # Exporta las clases principales del juego
    ├── block.py           # Clase base para los bloques
    ├── blocks.py          # Clases para cada tipo de bloque (I, J, L, O, S, T, Z)
    ├── colors.py          # Definición de colores
    ├── game.py            # Lógica principal del juego
    ├── grid.py            # Lógica y dibujo del grid/tablero
    └── position.py        # Clase para posiciones de celdas
```

## Requisitos

- pygame

Instala las dependencias con:

```bash
pip install pygame
```

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python main.py
```

## Características

1. Diseño del entorno gráfico con Pygame.
2. Lógica de creación y visualización del grid/tablero.
3. Lógica de creación y visualización de los bloques.
4. Lógica de movimiento de las piezas usando las teclas de cursor.
5. Lógica de colisión de bloques con las paredes del tablero.
6. Estructura modular: cada componente del juego está en su propio archivo y clase.
7. Configuración global del juego centralizada en `cfg/config.py`.

## Créditos

Proyecto educativo realizado por **ChechiDev** para practicar lógica y programación modular en Python con Pygame.
