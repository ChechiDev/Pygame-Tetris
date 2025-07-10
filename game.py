# game.py

from grid import Grid
from block import Block
from blocks import *
import random

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


    def _reset_blocks(self):
        """ Reset the list of available blocks """

        self._blocks = [
            IBlock(), JBlock(), LBlock(),
            OBlock(), SBlock(), TBlock(),
            ZBlock()
        ]


    def get_rdm_block(self):
        """ Returns a random block and removes it from the available blocks list """

        if len(self._blocks) == 0:
            self._reset_blocks()

        block = random.choice(self._blocks)
        self._blocks.remove(block) # Lo eliminamos de la lista para que no se repita o no esté disponible

        return block


    def move_left(self):
        """ Move the current block one cell to the left """
        self._current_block.move(0, -1)

        if self.block_inside() == False:
            self._current_block.move(0, 1) # Si se retorna false, devolvemos la pieza a la posición anterior


    def move_right(self):
        """ Move the current block one cell to the right """
        self._current_block.move(0, 1)

        if self.block_inside() == False:
            self._current_block.move(0, -1)


    def move_down(self):
        """ Move the current block one cell down """
        self._current_block.move(1, 0)

        if self.block_inside() == False:
            self._current_block.move(-1, 0)


    def rotate(self):
        self._current_block.rotate()


    def block_inside(self):
        """ Check if the current block is inside the grid boundaries """

        slots = self._current_block.get_cell_position()
        for slot in slots:
            if self._grid.is_inside(slot._row, slot._col) == False:
                return False

            return True


    def draw(self, screen):
        """ Draw the grid and the current block on the given screen surface """
        self._grid.draw(screen)
        self._current_block.draw(screen)