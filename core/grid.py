# grid.py

import pygame
from .colors import Colors

class Grid:
    """ Class representing the Tetris game grid """

    def __init__(self):
        """ Initialize with attr:grid size, cell size, and colors """

        # Lo primero que tenemos que saber del grid: rows, columns
        self._row = 20
        self._col = 10
        self._cell_size = 30 # valor en px para la celda
        # Creamos el grid
        self._grid = [[0 for _ in range(self._col)] for _ in range(self._row)]
        # Necesitamos saber los colores de las celdas:
        self._colors = Colors.get_cell_colors()


    # Dibujamos el grid:
    def print_grid(self) -> None:
        """ Print the grid """

        for r in self._grid:
            print(" ".join(str(cell) for cell in r)) # Printamos los 0 de cada  fila del grid con salto de linea.


    # Colition boundary checker
    def is_inside(self, row: int, col: int) -> bool:
        """
        Check if the given row and column are inside the grid boundaries.
        Return:
            True if inside, False otherwise.
        """

        # Check para ver si la pieza está dentro del grid
        if (row >= 0 and row < self._row) and (col >= 0 and col < self._col):
            return True

        return False


    def is_empty(self, row: int, col: int) -> bool:
        """ Return True if the specified cell is empty (value == 0) """

        # Checkeamos si la posicion del grid es 0
        if self._grid[row][col] == 0:
            return True

        return False


    def is_row_full(self, row: int) -> bool:

        # Recorremos todas las col de cada row:
        for col in range(self._col):
            # check para comprobar si la fila está completa:
            if self._grid[row][col] == 0:
                return False

        return True


    def clear_row(self, row: int) -> None:

        # Loop para poner la cell en 0
        for col in range(self._col):
            self._grid[row][col] = 0


    def set_row_down(self, row: int, num_rows: int) -> None:

        # Movemos la row indicada según el num_rows
        for col in range(self._col):
            # Copiamos los valores de cada row a la nueva poscion
            self._grid[row + num_rows][col] = self._grid[row][col]
            # Reset de la celda inicial a 0 (reset)
            self._grid[row][col] = 0


    def clear_all_rows(self) -> None:

        # Contador de filas completadas (full)
        check_full = 0
        # Check de todas las filas (abajo a arriba)
        for  row in range(self._row -1, 0, -1):
            # Si la row está full, limpiamos y sumamos check_full
            if self.is_row_full(row):
                self.clear_row(row)
                check_full += 1

            # si hay alguna row full, bajamos las rows superiores
            elif check_full > 0:
                self.set_row_down(row, check_full)

        # Retornamos el num de filas eliminadas
        return check_full


    def reset(self):
        """ Resets the grid by setting all cells to zero (0 = empty)"""

        for row in range(self._row):
            for col in range(self._col):
                self.grid[row][col] = 0


    def draw(self, screen) -> None: # Dibujamos el rectangulo de 'RECT'
        """ Draws the grid cells as rectangles on the given screen surface """

        for r in range(self._row):
            for c in range(self._col):
                cell_value = self._grid[r][c]

                # Dibujamos el objeto 'RECT' (el cuadrado que delimita la cell)
                # (x, y, w, h) => | x = col * tamaño de celda, y = row  * tamaño de celda, w(width) = tamaño de celda, h(height) = tamaño de celda
                # Reducimos 1px por cada lado con offset para que las lineas del grid sean visibles
                cell_rect = pygame.Rect(
                    c * self._cell_size + 1, # col, agregamos + 1 para agregar 1px offset (en total c tiene 31px)
                    r * self._cell_size + 1, # row, agregamos + 1 para agregar 1px offset
                    self._cell_size - 1, # Aqui quitamos 1px para convertir a 29 px (reducimos el cell)
                    self._cell_size - 1 # Aqui quitamos 1px para convertir a 29 px
                    )

                # importamos el pygame.rect(3 args => (surface(screen de la pantalla), color(lista de colores), rect))
                pygame.draw.rect(screen, self._colors[cell_value], cell_rect)
