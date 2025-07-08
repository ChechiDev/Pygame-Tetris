# grid.py

import pprint
import os
import pygame

class Grid:
    """ Class representing the Tetris game grid """
    def __init__(self):
        """ Initialize with attr:grid size, cell size, and colors """
        # Lo primero que tenemos que saber del grid: rows, columns
        self._row = 30
        self._col = 10
        self._cell_size = 30 # valor en px para la celda
        # Creamos el grid
        self._grid = [[0 for _ in range(self._col)] for _ in range(self._row)]
        # Necesitamos saber los colores de las celdas:
        self._colors = self.get_cell_colors()


    # Dibujamos el grid:
    def print_grid(self):
        """ Print the grid """

        for r in self._grid:
            print(" ".join(str(cell) for cell in r)) # Printamos los 0 de cada  fila del grid con salto de linea.


    def get_cell_colors(self):
        """Return a list of cell colors."""

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]


    def draw(self, screen): # Dibujamos el rectangulo de 'RECT'

        for r in range(self._row):
            for c in range(self._col):
                cell_value = self._grid[r][c]

                # Dibujamos el objeto 'RECT' (el cuadrado que delimita la cell)
                # (x, y, w, h) => | x = col * tamaño de celda, y = row  * tamaño de celda, w(width) = tamaño de celda, h(height) = tamaño de celda
                cell_rect = pygame.Rect(
                    c * self._cell_size + 1, # col, agregamos + 1 para agregar 1px offset (en total c tiene 31px)
                    r * self._cell_size + 1, # row, agregamos + 1 para agregar 1px offset
                    self._cell_size - 1, # Aqui quitamos 1px para convertir a 29 px (reducimos el cell)
                    self._cell_size - 1 # Aqui quitamos 1px para convertir a 29 px
                    )

                # importamos el pygame.rect(3 args => (surface(screen de la pantalla), color(lista de colores), rect))
                pygame.draw.rect(screen, self._colors[cell_value], cell_rect)


if __name__ == "__main__":
    os.system("cls")
    g = Grid()
    g.draw()
