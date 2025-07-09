# block.py

from colors import Colors

class Block:
    def __init__(self, id):
        self._id = id
        self._cells = {}
        self._cell_size = 30
        self._rotation = 0
        self._colors = Colors.get_cell_colors()

    # Metodo que se encargará de dibujar los blocks de las subclase:
    def draw(self, screen):
        slot = self._cells[self._rotation]



















if __name__ == "__main__":
    pass
    # b = Block()
    # print(b._colors)