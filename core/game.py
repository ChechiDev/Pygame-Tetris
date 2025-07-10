# game.py

import random
from .grid import Grid
from .block import Block
from .blocks import *

class Game():
    """ Container class for all the elements of the game """
    def __init__(self):
        self._grid = Grid()
        self._blocks = [
            IBlock(), JBlock(), LBlock(),
            OBlock(), SBlock(), TBlock(),
            ZBlock()
        ]
        self._current_block = self.get_rdm_block() # Escoge el block actual
        self._next_block = self.get_rdm_block() # Escoge el siguiente block


    def _reset_blocks(self) -> None:
        """ Reset the list of available blocks """

        self._blocks = [
            IBlock(), JBlock(), LBlock(),
            OBlock(), SBlock(), TBlock(),
            ZBlock()
        ]


    def get_rdm_block(self) -> Block:
        """ Returns a random block and removes it from the available blocks list """

        if len(self._blocks) == 0:
            self._reset_blocks()

        block = random.choice(self._blocks)
        self._blocks.remove(block) # Lo eliminamos de la lista para que no se repita o no esté disponible

        return block


    def move_left(self) -> None:
        """ Move the current block one cell to the left """
        self._current_block.move(0, -1)

        if self.block_inside() == False:
            self._current_block.move(0, 1) # Si se retorna false, devolvemos la pieza a la posición anterior


    def move_right(self) -> None:
        """ Move the current block one cell to the right """
        self._current_block.move(0, 1)

        if self.block_inside() == False:
            self._current_block.move(0, -1)


    def move_down(self) -> None:
        """ Move the current block one cell down """
        self._current_block.move(1, 0)

        if self.block_inside() == False:
            self._current_block.move(-1, 0)


    def rotate(self) -> None:
        """ Rotate the current block if the rotation keeps it inside the grid boundaries """

        self._current_block.rotate()

        if self.block_inside() == False:
            self._current_block.undo_rotate()

    def block_inside(self) -> bool:
        """ Check if the current block is inside the grid boundaries """

        slots = self._current_block.get_cell_position()
        for slot in slots:
            if self._grid.is_inside(slot._row, slot._col) == False:
                return False

        return True


    def draw(self, screen) -> None:
        """ Draw the grid and the current block on the given screen surface """

        self._grid.draw(screen)
        self._current_block.draw(screen)