# block.py

import pygame
from .colors import Colors
from .position import Position

class Block:
    def __init__(self, id):
        self._id = id
        self._cells = {}
        self._cell_size = 30
        self._row_offset = 0
        self._col_offset = 0
        self._rotation = 0
        self._colors = Colors.get_cell_colors()


    def move(self, rows: int, cols: int) -> None:
        """ Move the block by a given (arg) number of rows and columns """

        self._row_offset += rows
        self._col_offset += cols


    def get_cell_position(self) -> list[Position]:
        """ Get the current cell positions for the block's rotation """

        slot = self._cells[self._rotation]
        moved_pos = []

        for pos in slot:
            pos = Position(
                pos._row + self._row_offset,
                pos._col + self._col_offset
                )
            moved_pos.append(pos)

        return moved_pos


    def rotate(self) -> None:
        self._rotation += 1

        # Si rotamos todos los lados (len(cells)) del block, reiniciamos a 0
        if self._rotation == len(self._cells):
            self._rotation = 0


    # Método para impedir que rote cuando hay pared
    def undo_rotate(self) -> None:
        """ Undo the last rotation, cycling to the last rotation if needed """

        self._rotation -= 1

        if self._rotation == -1:
            self._rotation = len(self._cells) - 1


    # Metodo que se encargará de dibujar los blocks de las subclase:
    def draw(self, screen) -> None:
        """ Draw the block on the given screen surface """
        slots = self.get_cell_position()

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
