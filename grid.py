# grid.py

import pprint
import os

class Grid:
    def __init__(self):
        # Lo primero que tenemos que saber del grid: rows, columns
        self._row = 20
        self._col = 10
        self._cell_size = 30 # valor en px para la celda
        # Dibujamos el grid
        self._grid = [[0 for _ in range(self._col)] for _ in range(self._row)]



if __name__ == "__main__":
    os.system("cls")
    g = Grid()
    pprint.pprint(g._grid, indent=2)
