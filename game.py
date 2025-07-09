# game.py

from grid import Grid
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
