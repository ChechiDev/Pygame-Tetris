# block.py

import pygame
from colors import Colors

class Block:
    def __init__(self, id):
        self._id = id
        self._cells = {}
        self._cell_size = 30
        self._rotation = 0
        self._colors = Colors.get_cell_colors()

    # Metodo que se encargará de dibujar los blocks de las subclase:
    def draw(self, screen):
        slots = self._cells[self._rotation]

        # Generamos el cuadrado de la celda
        for slot in slots:
            slot_rect = pygame.Rect(
                slot._col * self._cell_size + 1,
                slot._row * self._cell_size + 1,
                self._cell_size - 1,
                self._cell_size - 1
            )

            # Dibujamos la celda:
            pygame.draw.rect(
                screen, # Fondo
                self._colors[self._id], # color del id block
                slot_rect # Dibujamos el cuadrado
                )
