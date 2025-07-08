# grid.py

import pprint
import os

class Grid:
    def __init__(self):
        # Lo primero que tenemos que saber del grid: rows, columns
        self._row = 20
        self._col = 10
        self._cell_size = 30 # valor en px para la celda
        # Creamos el grid
        self._grid = [[0 for _ in range(self._col)] for _ in range(self._row)]
        # Necesitamos saber los colores de las celdas:
        self._colors = self.get_cell_colors()


    # Dibujamos el grid:
    def print_grid(self):

        for r in self._grid:
            print(" ".join(str(cell) for cell in r)) # Printamos los 0 de cada  fila del grid con salto de linea.


    def get_cell_colors(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]




if __name__ == "__main__":
    os.system("cls")
    g = Grid()
    g.print_grid()
