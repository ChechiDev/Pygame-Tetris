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
            self.lock_block() # Si está bloqueado generamos block nuevo


    def lock_block(self):
        """
        Locks the current block in place by saving its cell positions to the grid.
        After locking, sets the next block as the current block and generates a new next block.
        """
        slots = self._current_block.get_cell_position()

        # Guardamos la posición de cada cell del block actual en el grid, usando su id
        for pos in slots:
            self._grid._grid[pos._row][pos._col] = self._current_block._id

        # Si llegamos a aqui es porque la posición del block anterior está bloqueada
        # Cambiamos el current_block por el siguiente y generamos un nuevo block random
        self._current_block = self._next_block
        self._next_block = self.get_rdm_block()



    def block_inside(self) -> bool:
        """ Check if the current block is inside the grid boundaries """

        return all(
            self._grid.is_inside(slot._row, slot._col)
            for slot in self._current_block.get_cell_position()
        )


    def rotate(self) -> None:
        """ Rotate the current block if the rotation keeps it inside the grid boundaries """

        self._current_block.rotate()

        if self.block_inside() == False:
            self._current_block.undo_rotate()


    def draw(self, screen) -> None:
        """ Draw the grid and the current block on the given screen surface """

        self._grid.draw(screen)
        self._current_block.draw(screen)