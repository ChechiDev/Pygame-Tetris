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
        self._game_over = False


    def _reset_blocks(self) -> None:
        """ Reset the list of available blocks """

        self._blocks = [
            IBlock(), JBlock(), LBlock(),
            OBlock(), SBlock(), TBlock(),
            ZBlock()
        ]


    def get_rdm_block(self) -> Block:
        """ Returns a random block and removes it from the available blocks list """

        # Si no quedan bloques disponibles en la lista:
        # reiniciamos para volver a tener todos los bloques
        if len(self._blocks) == 0:
            self._reset_blocks()

        block = random.choice(self._blocks)
        self._blocks.remove(block) # Lo eliminamos de la lista para que no se repita o no esté disponible

        return block


    def move_left(self) -> None:
        """ Move the current block one cell to the left """

        self._current_block.move(0, -1)

        if self.block_inside() == False or self.block_fits() == False:
            self._current_block.move(0, 1) # Si se retorna false, devolvemos la pieza a la posición anterior


    def move_right(self) -> None:
        """ Move the current block one cell to the right """

        self._current_block.move(0, 1)

        if self.block_inside() == False  or self.block_fits() == False:
            self._current_block.move(0, -1)


    def move_down(self) -> None:
        """ Move the current block one cell down """

        self._current_block.move(1, 0)

        # Si el current_block se sale del grid o no cabe en la posición nueva,
        # lo devolvemos a la posición anterior y lo bloqueamos en el grid
        if self.block_inside() == False or self.block_fits() == False:
            self._current_block.move(-1, 0)
            self.lock_block() # Si está bloqueado generamos block nuevo


    def lock_block(self):
        """
        Locks the current block in place by saving its cell positions to the grid.
        After locking, sets the next block as the current block and generates a new next block.
        """

         # Obtenemos todas las posiciones que ocupa el bloque actual
        slots = self._current_block.get_cell_position()

        # Guardamos la posición de cada cell del block actual en el grid, usando su id
        for pos in slots:
            self._grid._grid[pos._row][pos._col] = self._current_block._id

        # Si llegamos a aqui es porque la posición del block anterior está bloqueada
        # Cambiamos el current_block por el siguiente y generamos un nuevo block random
        self._current_block = self._next_block
        self._next_block = self.get_rdm_block()
        self._grid.clear_all_rows()

        # Si el block no cabe en el grid: Kill! Game over!
        if self.block_fits() == False:
            self._game_over = True



    def block_fits(self):
        """ Return True if all cells of the current block fit in empty grid positions """

        # Obtenemos todas las posiciones que ocupa el bloque actual
        slots = self._current_block.get_cell_position()

        # Recorremos cada celda del bloque
        for slot in slots:
            # Si alguna celda no está vacía en el grid, el bloque no cabe
            if self._grid.is_empty(slot._row, slot._col) == False:
                return False

        return True


    def block_inside(self) -> bool:
        """ Check if the current block is inside the grid boundaries """

        return all(
            self._grid.is_inside(slot._row, slot._col)
            for slot in self._current_block.get_cell_position()
        )


    def rotate(self) -> None:
        """ Rotate the current block if the rotation keeps it inside the grid boundaries """

        self._current_block.rotate()

        if self.block_inside() == False  or self.block_fits() == False:
            self._current_block.undo_rotate()


    def draw(self, screen) -> None:
        """ Draw the grid and the current block on the given screen surface """

        self._grid.draw(screen)
        self._current_block.draw(screen)